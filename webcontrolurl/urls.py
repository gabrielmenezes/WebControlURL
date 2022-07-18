from django.urls import path

from .views import HomeView,addUrlView
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path('', HomeView.as_view(), name="home"),
    path('AddUrl/', addUrlView.as_view(), name='addUrl'),
    path('AddMultipleURL/', views.addMultipleUrl, name='addMultipleURL'),
    #path('AddUrl/addRecord/', views.addRecord, name="addRecord"),
    
    #path('basededados/', views.aplicar, name="aplicar"),
]