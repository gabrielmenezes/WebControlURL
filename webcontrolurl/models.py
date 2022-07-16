from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=255, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    oficio = models.CharField(max_length=255)
    chamado = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.url
