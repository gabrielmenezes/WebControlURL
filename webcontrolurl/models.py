from django.urls import reverse
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=255, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    oficio = models.CharField(max_length=255)
    chamado = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('home')

class DeletedUrl(models.Model):
    url = models.CharField(max_length=255)
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.url + '|' + self.usuario.username
