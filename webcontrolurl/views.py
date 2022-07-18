from cmath import exp
from django.views.generic import ListView, CreateView
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError

import csv
from .models import Url
from .forms import UrlForm

class HomeView(ListView):
        model = Url
        template_name = 'webcontrolurl/home.html'

class addUrlView(CreateView):
        model = Url
        form_class = UrlForm
        template_name = 'webcontrolurl/addUrl.html'

def addMultipleUrl(request):
        if request.method == 'GET':
                template = loader.get_template('webcontrolurl/addMultipleUrl.html')
                return HttpResponse(template.render({}, request))
        elif request.method == 'POST':
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="result.csv"'},
                )
                writer = csv.writer(response)
                #Pegar arquivo e usuario enviado na requisição
                csv_file = request.FILES['csv_file']
                user_id = request.user
                #decodificar arquivo
                file_data = csv_file.read().decode('utf-8-sig')
                #separar em linhas
                lines = file_data.split('\n')
                #Para cada linha, gera a entrada no banco de dados
                for line in lines:
                        fields = line.split(';')
                        
                        #Retira se houver o cabeçalho
                        if fields[0] == "URLs":
                                continue
                        #Senão verifica se esta vazio
                        if fields[0] == '':
                                continue 
                        #Caso seja uma Url, verifica se salva no Banco.
                        url = Url(url=fields[0],oficio=fields[1],chamado=fields[2],usuario=user_id)

                        try:
                                url.full_clean()
                        except ValidationError as e:
                                writer.writerow([fields[0], e])
                                continue

                        url.save()
                        writer.writerow([fields[0], 'sucess'])

                return response