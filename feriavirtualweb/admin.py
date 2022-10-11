from django.contrib import admin

# Register your models here.
from . models import Producto,Region,User

admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(User)