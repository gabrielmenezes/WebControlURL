from django.views.generic import ListView, CreateView

from .models import Url
from .forms import UrlForm

class HomeView(ListView):
        model = Url
        template_name = 'webcontrolurl/home.html'

class addUrlView(CreateView):
        model = Url
        form_class = UrlForm
        template_name = 'webcontrolurl/addUrl.html'
        #fields = '__all__'


#def addMultipleUrl(request):
 #       template = loader.get_template('webcontrolurl/addMultipleUrl.html')
  #      return HttpResponse(template.render({}, request))

#def addMultipleUrls(request):
#       csv_file = request.FILES['csv_file']

#        file_data = csv_file.read().decode('utf-8-sig')

#        lines = file_data.split('\n')

#       for line in lines:
#               fields = line.split(';')
                #Verifica cabecalho
#               if fields[0] == "URLs":
#                       continue
#               if fields[0] == '':
 #                       continue 

  #              url = Url(url=fields[0],oficio=fields[1],chamado=fields[2])
   #             url.save()

    #    urls = Url.objects.all()
     #   filename = "baseurls.txt"
      #  f = open(filename, mode = "w")

       # for url in urls:
        #        f.write("\n" + url.url)

        #return HttpResponseRedirect('/')