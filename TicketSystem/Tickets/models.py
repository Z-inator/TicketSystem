from django.db import models
from django.forms import ModelForm
from datetime import datetime


# Create your models here.
class Ticket(models.Model):
    title = models.CharField('title', max_length=100)
    name = models.CharField('name', max_length=100)
    contact = models.EmailField('contact', max_length=200)
    submissionDate = models.DateTimeField('date submitted', default=datetime.now, blank=True)
    description = models.TextField('description')
    highPriority = models.BooleanField('high priority', default=None)

    def __str__(self):
        return self.title

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['submissionDate']

