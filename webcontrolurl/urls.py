from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('AddUrl/', views.addUrl, name='AddUrl'),
    path('AddUrl/addRecord/', views.addRecord, name="addRecord"),
    path('addMultipleUrl/', views.addMultipleUrl, name="addMultipleUrl"),
    path('addMultipleUrl/add/', views.addMultipleUrls, name="addMultipleUrls"),
    path('basededados/', views.aplicar, name="aplicar"),
]