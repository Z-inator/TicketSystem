from django.db import models
from django.forms import modelformset_factory
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
            instance = form.save()
            # instance_id = instance.id
            # request.session['instance_id'] = instance_id
            # return redirect('../thanks/')
            return redirect('submit', pk=instance.pk)
            # ../thanks/

            # tickets = Ticket.objects.all()
            # return HttpResponseRedirect(reverse('Tickets:thanks'))
            # return render(request, 'Tickets/thanks.html', {'instance': instance})

    else:
        form = TicketForm()
    return render(request, 'Tickets/form.html', {'form': form})

    # return render(request, 'Tickets/form.html', {'form': form,})


def submit(request, pk):
    # tickets = Ticket.objects.all()
    # ticket_id = request.GET.get('instance')
    # instance_id = request.session.get('instance_id')
    # instance_id = instance.id
    tickets = get_object_or_404(Ticket, pk=pk)
    
    return render(request, 'Tickets/submission.html', {'tickets':tickets})

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