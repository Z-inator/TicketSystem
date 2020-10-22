from django.shortcuts import render
from .models import TicketForm, Ticket
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'Tickets/index.html', )

def form(request):
   # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TicketForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            issue = Ticket(title=request.POST.get('title', ''), 
              name=request.POST.get('name', ''),
              contact=request.POST.get('contact', ''), 
              submissionDate=timezone.now(), 
              description=request.POST.get('description', ''), 
              highPriority=request.POST.get('highPriority', ''))
            issue.save()
            # redirect to a new URL:
            return HttpResponseRedirect('templates/Tickets/thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        print("Use correct format.")
        form = TicketForm()

    return render(request, 'Tickets/form.html', {'form': form})

class thanks(generic.DetailView):
    model = Ticket
    template_name = 'Tickets/thanks.html'

