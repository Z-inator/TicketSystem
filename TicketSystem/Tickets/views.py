from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.urls import reverse

# Create your views here.

from .models import Ticket, TicketForm


# Create your views here.
def index(request):
    return render(request, 'Tickets/index.html', )

def form(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            tickets = Ticket.objects.all()
            # return HttpResponseRedirect(reverse('Tickets:thanks'))
            return render(request, 'Tickets/thanks.html', {'tickets': tickets})

    else:
        form = TicketForm
        return render(request, 'Tickets/form.html', {'form': form,})

    # return render(request, 'Tickets/form.html', {'form': form,})


# def thanks(request):
#     tickets = Ticket.objects.all()
#     return render(request, 'Tickets/thanks.html', )

# def processForm(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse("Your data has been entered")
#             return render(request, 'Tickets/thanks.html', )

#     else:
#         form = TicketForm

#     return render(request, 'Tickets/form.html', {'form': form,})