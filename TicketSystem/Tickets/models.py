from django.db import models
from datetime import datetime
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, related_name="tickets",on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    submissionDate = models.DateTimeField('Date Submitted', auto_now=True)
    description = models.TextField('Description')
    highPriority = models.BooleanField('High Priority', default=None, help_text="Is this issue urgent?")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'Tickets:single', 
            kwargs={
                'pk':self.pk
            }
        )
    
    class Meta:
        ordering = ['-submissionDate']
        unique_together = ['user', 'title']
