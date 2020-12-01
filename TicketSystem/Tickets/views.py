from django.db import models
from django.forms import modelformset_factory
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

# Create your views here.

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class Dashboard(generic.ListView):
    model = models.Ticket
    template_name = 'Tickets/ticket_dashboard.html'


class CreateTicket(generic.CreateView):
    # Use this for more complicated forms: explicit call
    form_class = forms.TicketForm
    # Use this for basic forms: Django automatically created model form from model
    # model = models.Ticket
    # fields = ('title', 'description', 'highPriority')
    template_name = 'Tickets/ticket_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TicketList(generic.ListView):
    model = models.Ticket
    context_object_name = 'ticket_list'

    def get_queryset(self):
        try:
            self.ticket_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.ticket_user.tickets.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket_user"] = self.ticket_user
        return context

class TicketDetail(generic.DetailView):
    model = models.Ticket
    context_object_name = 'ticket_detail'
    template_name = 'Tickets/ticket_detail.html'

class TicketUpdate(generic.UpdateView):
    model = models.Ticket
    fields = ['title','firstName','lastName','contact','description','highPriority']
    template_name = 'Tickets/ticket_update.html'
    context_object_name = 'ticket_detail_update'

    def get_success_url(self):
        return reverse_lazy('Tickets:all')

class TicketDelete(generic.DeleteView):
    model = models.Ticket
    success_url = reverse_lazy('Tickets:all')
