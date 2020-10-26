from django.contrib import admin
from .models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['title']}),
        ('Submission Date',   {'fields': ['submissionDate'], 'classes': ['collapse']}),
    ]
    # inlines = [ChoiceInLine]
    list_display = ('title', 'submissionDate', 'name', 'contact', 'highPriority')
    list_filter = ['submissionDate']
    search_fields = ['contact']

admin.site.register(Ticket, TicketAdmin)