from django import forms
from .models import Url

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