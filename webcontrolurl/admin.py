from django.contrib import admin

from .models import Url, DeletedUrl
# Register your models here.

admin.site.register(Url)
#admin.site.register(DeletedUrl)


class DeletedUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'usuario', 'created_at')

admin.site.register(DeletedUrl, DeletedUrlAdmin)