from django.contrib import admin

from .models import BlockedIp, DeletedIp, Url, DeletedUrl
# Register your models here.

admin.site.register(Url)
admin.site.register(BlockedIp)


class DeletedUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'usuario', 'created_at')

class DeletedIpAdmin(admin.ModelAdmin):
    list_display = ('ip', 'usuario', 'created_at')

admin.site.register(DeletedUrl, DeletedUrlAdmin)
admin.site.register(DeletedIp, DeletedIpAdmin)