from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Album, Gallery
# Register your models here.

admin.site.register(Album)
admin.site.register(Gallery)