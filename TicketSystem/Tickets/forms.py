from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = (
            'title',
            'firstName',
            'lastName',
            'contact',
            'description',
            'highPriority'
        )


        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'Ticket Title'
        #         }
        #     ),
        #     'firstName': forms.TextInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'John'
        #         }
        #     ),
        #     'lastName': forms.TextInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'Smith'
        #         }
        #     ),
        #     'contact': forms.EmailInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'email@email.com'
        #         }
        #     ),
        #     'description': forms.Textarea(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'Please describe your issue in detail...'
        #         }
        #     ),
        #     'highPriority': forms.CheckboxInput(
        #         attrs={
        #             'class': 'form-control',
        #             'class': 'form-check',
        #             'class': 'form-text text-muted'
        #         }
        #     ),
        # }

