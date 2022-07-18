from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webcontrolurl.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]