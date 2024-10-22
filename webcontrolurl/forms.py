import ipaddress
from django import forms
from .models import Url,BlockedIp

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url', 'usuario', 'oficio', 'chamado')

        widgets = {
            'url': forms.TextInput(attrs={'class':'form-control','placeholder':'Coloque a url, sem www como "google.com"'}),
            'oficio': forms.TextInput(attrs={'class':'form-control'}),
            'chamado': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control', 'id':'user', 'value':'', 'type':'hidden'}),
        }

class IpForm(forms.ModelForm):
    class Meta:
        model = BlockedIp
        fields = ('ip', 'usuario', 'oficio', 'chamado')

        widgets = {
            'ip': forms.TextInput(attrs={'class':'form-control','placeholder':'Coloque o IP, como "192.168.2.0/24"'}),
            'oficio': forms.TextInput(attrs={'class':'form-control'}),
            'chamado': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control', 'id':'user', 'value':'', 'type':'hidden'}),
        }

    def clean_ip(self):
        new_ip = self.cleaned_data.get('ip')

        try:
            new_network = ipaddress.ip_network(new_ip, strict=False)
        except ValueError:
            raise forms.ValidationError('O endereço IP informado não é valido.')
        
        for ip_control in BlockedIp.objects.all():
            existing_network = ipaddress.ip_network(ip_control.ip, strict=False)
            if (new_network.overlaps(existing_network)):
                raise forms.ValidationError(
                    f"A rede {new_network} sobrepõe a rede existente: {existing_network}"
                )
        return new_network