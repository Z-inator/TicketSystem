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
        """Returns a list of all field names on the instance."""
        fields = []
        for field in self._meta.fields:
            field_name = field.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+field_name+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, field_name)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if field.editable and value and field_name not in ('id') :

                fields.append(
                {
                    'label':field.verbose_name, 
                    'name':field.name, 
                    'value':value,
                }
                )
        return fields
