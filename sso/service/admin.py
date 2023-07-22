from django.contrib import admin
from .models import Service, Connection


class ServiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ConnectionAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'service')
    list_display_links = ('id', 'user', 'service')



admin.site.register(Service, ServiceAdmin)
admin.site.register(Connection, ConnectionAdmin)

