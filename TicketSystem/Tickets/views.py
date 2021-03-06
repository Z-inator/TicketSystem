from django.db import models
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .forms import TicketForm
from .models import Ticket

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class Dashboard(LoginRequiredMixin, generic.ListView):
    model = Ticket
    template_name = "Tickets/ticket_dashboard.html"

class CreateTicket(LoginRequiredMixin, generic.CreateView):
    # Use this for more complicated forms: explicit call
    form_class = TicketForm
    # Use this for basic forms: Django automatically created model form from model
    # model = models.Ticket
    # fields = ("title", "description", "highPriority")
    template_name = "Tickets/ticket_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TicketList(LoginRequiredMixin, generic.ListView):
    model = Ticket
    template_name = "Tickets/ticket_list.html"

    def get_queryset(self):
        self.user.username = get_object_or_404(Ticket, user=self.kwargs['user'])
        return Ticket.objects.filter(user=self.user)

    def get_context_data(self):
        context = super().get_context_data(**kwargs)
        context["user"] = self.user
        return context

    # def get_queryset(self):
    #     try:
    #         user_tickets = Ticket.objects.filter(self.user="username")
    #     except User.DoesNotExist:
    #         raise Http404
    #     else:
    #         return user_tickets

    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context["Ticket_user"] = user_tickets
    #         return context

    # def get_queryset(self):
    #     try:
    #         self.ticket_user = User.objects.prefetch_related("tickets").get(
    #             username__iexact=self.kwargs.get("username")
    #         )
    #     except User.DoesNotExist:
    #         raise Http404
    #     else:
    #         return self.ticket_user.tickets.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["ticket_user"] = self.ticket_user
    #     return context

class TicketDetail(LoginRequiredMixin, generic.DetailView):
    model = Ticket
    template_name = "Tickets/ticket_detail.html"

class TicketUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Ticket
    fields = ["title","description","highPriority"]
    template_name = "Tickets/ticket_update.html"

    def get_success_url(self):
        return reverse_lazy("Tickets:all")

class TicketDelete(LoginRequiredMixin, generic.DeleteView):
    model = Ticket
    success_url = reverse_lazy("Tickets:all")
