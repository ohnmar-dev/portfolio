from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Album, Gallery, Category, Blog
# Register your models here.

admin.site.register(Album)
admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(Blog)