from django.urls import path
from . import views

app_name = 'Tickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.index, name='form'),
    path('thanks/', views.thanks, name='thanks'),
    path('upload/', views.upload, name='upload'),
]