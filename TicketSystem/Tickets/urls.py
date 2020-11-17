from django.urls import path
from . import views

app_name = 'Tickets'

urlpatterns = [
    path('', views.TicketList.as_view(), name='all'),
    path('new/', views.CreateTicket.as_view(), name='new'),
    path('<int:pk>/', views.TicketDetail.as_view(), name='single'),
    # path('thanks/', views.thanks, {'instance_id': 'instance_id'},name='thanks'),
]
