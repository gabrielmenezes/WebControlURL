from django.urls import path

from .views import HomeView,addUrlView
from . import views

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('AddUrl/', addUrlView.as_view(), name='addUrl'),
    path('AddMultipleURL/', views.addMultipleUrl, name='addMultipleURL'),
    path('deleteMultipleURL/', views.deleteMultipleUrl, name='deleteMultipleURL'),
    path('auditRemoverUrl/<int:pk>',views.removerUrl, name='audit_remove_url'),
    path('basededados/', views.aplicar, name="aplicar"),

]