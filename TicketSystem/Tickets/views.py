from django.db import models
from django.forms import modelformset_factory
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views import generic

# Create your views here.

from . import forms
from . import models


# Create your views here.

# def index(request):
#     return render(request, 'Tickets/index.html', )

class CreateTicket(generic.CreateView):
    model = models.Ticket
    fields = ('title','firstName','lastName','contact','description','highPriority')

class TicketList(generic.ListView):
    model = models.Ticket
    context_object_name = 'ticket_list'

class TicketDetail(generic.DetailView):
    model = models.Ticket
    context_object_name = 'ticket_detail'

    # def get(self, *args, **kwargs):
    #     fields = forms.TicketForm(data=model_to_dict(models.Tickets.objects.get(pk=self.kwargs.get('pk'))))
    #     return super().get(*args, **kwargs)


# def form(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance_id = instance.id
#             request.session['instance_id'] = instance_id
#             return redirect('../thanks/')
#             # ../thanks/

#             # tickets = Ticket.objects.all()
#             # return HttpResponseRedirect(reverse('Tickets:thanks'))
#             # return render(request, 'Tickets/thanks.html', {'instance': instance})

#     else:
#         form = TicketForm
#         return render(request, 'Tickets/form.html', {'form': form,})

#     # return render(request, 'Tickets/form.html', {'form': form,})


# def thanks(request, instance_id):
#     # tickets = Ticket.objects.all()
#     # ticket_id = request.GET.get('instance')
#     instance_id = request.session.get('instance_id')
#     tickets = get_object_or_404(Ticket, pk=instance_id)
    
#     return render(request, 'Tickets/thanks.html', {'tickets':tickets})

# # def processForm(request):
# #     if request.method == 'POST':
# #         form = TicketForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             # return HttpResponse("Your data has been entered")
# #             return render(request, 'Tickets/thanks.html', )

# #     else:
# #         form = TicketForm

# #     return render(request, 'Tickets/form.html', {'form': form,})