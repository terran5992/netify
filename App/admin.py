from django.contrib import admin

# Register your models here.

from .models import Source, Record

# Adding the table to the admin interface
admin.site.register(Source)
admin.site.register(Record)