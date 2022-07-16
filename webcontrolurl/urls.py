from django.urls import path

from . import views
from .views import HomeView

urlpatterns = [
    #path("", views.index, name="index"),
    path('', HomeView.as_view(), name="home"),
    #path('AddUrl/', views.addUrl, name='AddUrl'),
    #path('AddUrl/addRecord/', views.addRecord, name="addRecord"),
    #path('addMultipleUrl/', views.addMultipleUrl, name="addMultipleUrl"),
    #path('addMultipleUrl/add/', views.addMultipleUrls, name="addMultipleUrls"),
    #path('basededados/', views.aplicar, name="aplicar"),
]