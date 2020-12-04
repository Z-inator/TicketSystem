from django.db import models
from datetime import datetime
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Ticket(models.Model):
    user = models.ForeignKey(User, related_name="tickets", on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=100)
    submissionDate = models.DateTimeField("Date Submitted", auto_now=True)
    description = models.TextField("Description")
    highPriority = models.BooleanField("High Priority", default=None, help_text="Is this issue urgent?")

    class Meta:
        ordering = ["-submissionDate"]
        unique_together = ["user", "title"]     # Consider removing so someone can use the same name for a ticket

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "Tickets:single", 
            kwargs={
                "pk":self.pk,
                "username":self.user.username
            }
        )
    
    # Provided by shacker on Stackoverflow
    def get_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for field in self._meta.fields:
            field_name = field.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = "get_"+field_name+"_display"
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, field_name)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if value and field_name not in ("id") :

                fields.append(
                {
                    "label":field.verbose_name, 
                    "name":field.name, 
                    "value":value,
                }
                )
        return fields
