from django.contrib import admin

# Register your models here.

from django.db import models

# Create your models here.

from . models import Guest

class TampilGuest(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'kegiatan')
    list_display_links = (None)
    search_fields = ('nim', 'nama')

admin.site.register(Guest, TampilGuest)