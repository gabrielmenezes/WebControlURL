from django.urls import path

from .views import HomeView, addUrlView, addIpView, listIp
from . import views

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('listip/', listIp.as_view(), name="listip"),
    path('AddUrl/', addUrlView.as_view(), name='addUrl'),
    path('AddIp/', addIpView.as_view(), name='addIp'),
    path('auditRemoverIp/<int:pk>',views.removerIp, name='audit_remove_ip'),
    path('AddMultipleURL/', views.addMultipleUrl, name='addMultipleURL'), 
    path('AddMultipleIp/', views.addMultipleIp, name='addMultipleIp'), 
    path('deleteMultipleURL/', views.deleteMultipleUrl, name='deleteMultipleURL'),
    path('deleteMultipleIp/', views.deleteMultipleIp, name='deleteMultipleIp'),
    path('auditRemoverUrl/<int:pk>',views.removerUrl, name='audit_remove_url'),
    path('basededados/', views.aplicar, name="aplicar"),
    path('basedeips/', views.getAllIps, name='getAllIps'),

]