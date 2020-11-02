from django.db import models
from django import forms
from datetime import datetime


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

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['submissionDate']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ticket Title'
                }
            ),
            'firstName': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'John'
                }
            ),
            'lastName': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Smith'
                }
            ),
            'contact': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'email@email.com'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Please describe your issue in detail...'
                }
            ),
            'highPriority': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'class': 'form-check',
                    'class': 'form-text text-muted'
                }
            ),
        }

