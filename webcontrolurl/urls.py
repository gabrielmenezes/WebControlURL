from django.urls import path

from .views import HomeView,addUrlView

urlpatterns = [
    #path("", views.index, name="index"),
    path('', HomeView.as_view(), name="home"),
    path('AddUrl/', addUrlView.as_view(), name='addUrl'),
    #path('AddUrl/addRecord/', views.addRecord, name="addRecord"),
    #path('addMultipleUrl/', views.addMultipleUrl, name="addMultipleUrl"),
    #path('addMultipleUrl/add/', views.addMultipleUrls, name="addMultipleUrls"),
    #path('basededados/', views.aplicar, name="aplicar"),
]