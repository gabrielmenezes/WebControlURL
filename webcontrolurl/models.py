from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=255)
    oficio = models.CharField(max_length=255)
    chamado = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)