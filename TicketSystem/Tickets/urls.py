from django.urls import path
from . import views

app_name = 'Tickets'

urlpatterns = [
    path('', views.TicketList.as_view(), name='all'),
    path('<username>/dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('new/', views.CreateTicket.as_view(), name='create'),
    path('<username>/<int:pk>/', views.TicketDetail.as_view(), name='single'),
    path('<username>/<int:pk>/update/', views.TicketUpdate.as_view(), name='update'),
    path('<username>/<int:pk>/delete/', views.TicketDelete.as_view(), name='delete'),
]
