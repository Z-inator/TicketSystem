from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.
class Ticket(models.Model):
    title = models.CharField('Title', max_length=100)
    firstName = models.CharField('First Name', max_length=100)
    lastName = models.CharField('Last Name', max_length=100)
    contact = models.EmailField('Email', max_length=200)
    submissionDate = models.DateTimeField('Date Submitted', default=datetime.now, blank=True)
    description = models.TextField('Description')
    highPriority = models.BooleanField('High Priority', default=None, help_text="Is this issue urgent?")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('Tickets:single', kwargs={'pk':self.pk})
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Ticket._meta.fields]