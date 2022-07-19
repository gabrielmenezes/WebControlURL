from django.urls import path

from .views import HomeView,addUrlView
from . import views

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('AddUrl/', addUrlView.as_view(), name='addUrl'),
    #path('url/<int:pk>/remove', DeleteUrlView.as_view(), name='remove_url'),
    path('AddMultipleURL/', views.addMultipleUrl, name='addMultipleURL'),
    path('auditRemoverUrl/<int:pk>',views.removerUrl, name='audit_remove_url'),
    #path('basededados/', views.aplicar, name="aplicar"),

]