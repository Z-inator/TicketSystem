from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = (
            "title",
            "description",
            "highPriority"
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["ticket"].queryset = (
                models.Ticket.objects.filter(
                    pk__in=user.tickets.values_list("ticket__pk")
                )
            )