from django.urls import path
from . import views

app_name = 'Tickets'

urlpatterns = [
    path('', views.TicketList.as_view(), name='all'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('new/', views.CreateTicket.as_view(), name='create'),
    path('<int:pk>/', views.TicketDetail.as_view(), name='single'),
    path('<int:pk>/update/', views.TicketUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.TicketDelete.as_view(), name='delete'),
]
