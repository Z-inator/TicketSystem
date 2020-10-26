from django.urls import path
from . import views

app_name = 'Tickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('thanks/', views.thanks, name='thanks'),
]
