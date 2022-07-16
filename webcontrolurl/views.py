from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

from webcontrolurl.models import Url

class HomeView(ListView):
        model = Url
        template_name = 'webcontrolurl/home.html'

def addUrl(request):
        template = loader.get_template('webcontrolurl/addUrl.html')
        return HttpResponse(template.render({}, request))

def addRecord(request):

        #Capturando dados enviados no POST
        u = request.POST['url']
        o = request.POST['oficio']
        c = request.POST['chamado']
        
        newUrl = Url(url=u,oficio=o,chamado=c)
        newUrl.save()
        
	#TESTE
        urls = Url.objects.all()
        filename = "baseurls.txt"
        f = open(filename, mode = "w")

        for url in urls:
                f.write("\n" + url.url)
        
        return HttpResponseRedirect('/')

def addMultipleUrl(request):
        template = loader.get_template('webcontrolurl/addMultipleUrl.html')
        return HttpResponse(template.render({}, request))

def addMultipleUrls(request):
        csv_file = request.FILES['csv_file']

        file_data = csv_file.read().decode('utf-8-sig')

        lines = file_data.split('\n')

        for line in lines:
                fields = line.split(';')
                #Verifica cabecalho
                if fields[0] == "URLs":
                        continue
                if fields[0] == '':
                        continue 

                url = Url(url=fields[0],oficio=fields[1],chamado=fields[2])
                url.save()

        urls = Url.objects.all()
        filename = "baseurls.txt"
        f = open(filename, mode = "w")

        for url in urls:
                f.write("\n" + url.url)

        return HttpResponseRedirect('/')

def aplicar(request):
        filename = "baseurls.txt"
        f = open(filename, 'rb')

        response = FileResponse(f)

        return response
