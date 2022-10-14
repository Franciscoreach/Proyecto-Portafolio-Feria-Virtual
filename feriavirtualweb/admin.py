from django.contrib import admin
from . models import Producto,Categoria,Pedido,User

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precioKilo","categoria"]
    #list_editable = ["precio"]
    #search_fields = ["nombre","precio","propietario"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["idUsuario","email","username","tipo_usuario","con_contrato"]
    #search_fields = ["idUsuario","email","username","tipo_usuario","con_contrato"]
    #list_filter = ["tipo_usuario","con_contrato"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(User,UsuarioAdmin)
admin.site.register(Pedido)
admin.site.register(Categoria)