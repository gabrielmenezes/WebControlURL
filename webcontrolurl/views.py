from xml.dom import ValidationErr
from django.views.generic import ListView, CreateView
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

import csv
from .models import Url, DeletedUrl, BlockedIp , DeletedIp
from .forms import UrlForm, IpForm

class HomeView(ListView):
        model = Url
        template_name = 'webcontrolurl/home.html'

class listIp(ListView):
        model = BlockedIp
        template_name = 'webcontrolurl/ips.html'

class addUrlView(CreateView):
        model = Url
        form_class = UrlForm
        template_name = 'webcontrolurl/addUrl.html'

class addIpView(CreateView):
        model = BlockedIp
        form_class = IpForm
        template_name = 'webcontrolurl/addIp.html'

def addMultipleUrl(request):
        if request.method == 'GET':
                template = loader.get_template('webcontrolurl/addMultipleUrl.html')
                return HttpResponse(template.render({}, request))
        elif request.method == 'POST':
                #Cria Resposta
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="result.csv"'},
                )
                #Stream para escrever a resposta.
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


def addMultipleIp(request):
        if request.method == 'GET':
                template = loader.get_template('webcontrolurl/addMultipleIp.html')
                return HttpResponse(template.render({}, request))
        elif request.method == 'POST':
                #Cria Resposta
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="result.csv"'},
                )
                #Stream para escrever a resposta.
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
                        if fields[0] == "IPs":
                                continue
                        #Senão verifica se esta vazio
                        if fields[0] == '':
                                continue 
                        #Caso seja um IP, verifica se salva no Banco.
                        ip = BlockedIp(ip=fields[0],oficio=fields[1],chamado=fields[2],usuario=user_id)

                        try:
                                ip.clean()
                        except Exception as e:
                                writer.writerow([fields[0], e])
                                continue

                        ip.save()
                        writer.writerow([fields[0], 'sucess'])

                return response

def deleteMultipleIp(request):
        if request.method == 'GET':
                template = loader.get_template('webcontrolurl/deleteMultipleIp.html')
                return HttpResponse(template.render({}, request))
        elif request.method == 'POST':
                #Cria Resposta
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="result.csv"'},
                )
                #Stream para escrever a resposta.
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
                        #Retira se houver o cabeçalho
                        if line == "IPs":
                                continue
                        #Senão verifica se esta vazio
                        if line == '':
                                continue 
                        #Caso seja uma Url, verifica se salva no Banco.
                        try:
                                ip = BlockedIp.objects.get(ip=line.strip())
                                audit = DeletedIp(ip=ip.ip,usuario=user_id)
                        except:
                                writer.writerow([line, 'IP nao encontrado'])
                                continue

                        try:
                                audit.full_clean()
                                ip.delete()
                                writer.writerow([line, 'sucess'])
                        except Exception as e:
                                writer.writerow([line, e])
                                continue
                return response
        
def deleteMultipleUrl(request):
        if request.method == 'GET':
                template = loader.get_template('webcontrolurl/deleteMultipleUrl.html')
                return HttpResponse(template.render({}, request))
        elif request.method == 'POST':
                #Cria Resposta
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="result.csv"'},
                )
                #Stream para escrever a resposta.
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
                        #Retira se houver o cabeçalho
                        if line == "URLs":
                                continue
                        #Senão verifica se esta vazio
                        if line == '':
                                continue 
                        #Caso seja uma Url, verifica se salva no Banco.
                        try:
                                url = Url.objects.get(url=line.strip())
                                audit = DeletedUrl(url=url.url,usuario=user_id)
                        except:
                                writer.writerow([line, 'URL nao encontrada'])
                                continue

                        try:
                                audit.full_clean()
                                url.delete()
                                writer.writerow([line, 'sucess'])
                        except ValidationError as e:
                                writer.writerow([line, e])
                                continue
                return response

def removerUrl(request, pk):
        if request.method == 'GET':
               #Carrega página a renderizar
               template = loader.get_template('webcontrolurl/removeUrl.html')
               #Pega URL a ser removida
               url = Url.objects.get(pk=pk)
               #Inseri a URL no contexto
               context = {
                       'url': url,
               }
               #Retorna a página para seguir com a deleção
               return HttpResponse(template.render({}, request))

        if request.method == 'POST':
                #Pega URL a ser deletada
                url = Url.objects.get(pk=pk)
                user = request.user
                audit = DeletedUrl(url=url.url,usuario=user)

                #Verifica se tem problemas para salvar a auditoria no banco
                try:
                        audit.full_clean()
                except ValidationError as e:
                        return HttpResponseBadRequest('Falha no sistema de auditoria a URL %s' % e)

                #Se nao houver problemas, salva e remove a URL
                audit.save()
                url.delete()


                response = redirect('home')
                return response


def removerIp(request, pk):
        if request.method == 'GET':
               #Carrega página a renderizar
               template = loader.get_template('webcontrolurl/removeIp.html')
               #Pega URL a ser removida
               ip = BlockedIp.objects.get(pk=pk)
               #Inseri a URL no contexto
               context = {
                       'ip': ip,
               }
               #Retorna a página para seguir com a deleção
               return HttpResponse(template.render({}, request))

        if request.method == 'POST':
                #Pega URL a ser deletada
                ip = BlockedIp.objects.get(pk=pk)
                user = request.user
                audit = DeletedIp(ip=ip.ip,usuario=user)

                #Verifica se tem problemas para salvar a auditoria no banco
                try:
                        audit.full_clean()
                except ValidationError as e:
                        return HttpResponseBadRequest('Falha no sistema de auditoria ao IP %s' % e)

                #Se nao houver problemas, salva e remove a URL
                audit.save()
                ip.delete()

                response = redirect('home')
                return response

def aplicar(request):
        #pegar todas urls
        urls = Url.objects.all()
        
        #inicializar resposta
        content = ''

        #iterar sobre cada url para cadastrar no arquivo
        for url in urls:
                content+=url.url+'\n'
                content+='*.'+url.url+'\n'
        
        #responder o arquivo.
        return HttpResponse(content, content_type='text/plain')

def getAllIps(request):
        ips = BlockedIp.objects.all()

        content = ''

        for ip in ips:
                content+=ip.ip+'\n'
        
        return HttpResponse(content,content_type='text/plain')