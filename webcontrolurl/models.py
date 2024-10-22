import ipaddress
from os import error
from xml.dom import ValidationErr
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

class DeletedIp(models.Model):
    ip = models.CharField(max_length=255)
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ip + '|' + self.usuario.username

class BlockedIp(models.Model):
    ip = models.CharField(max_length=43) # Ex: '192.168.30.0/24' 
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    oficio = models.CharField(max_length=255)
    chamado = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def clean(self):
        new_ip = self.ip

        try:
            new_network = ipaddress.ip_network(new_ip, strict=False)
        except ValueError:
            raise ValidationErr('O endereço IP informado não é valido.')
        
        for ip_control in BlockedIp.objects.all():
            existing_network = ipaddress.ip_network(ip_control.ip, strict=False)
            if (new_network.overlaps(existing_network)):
                raise ValidationErr(
                    f"A rede {new_network} sobrepõe a rede existente: {existing_network}"
                )
        return new_network

    def __str__(self):
        return self.ip
    
    def get_absolute_url(self):
        return reverse('home')