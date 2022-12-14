from django.contrib import admin
from . models import Producto,Categoria,User,SubastaProducto,SolicitudProducto,TransporteProducto,Pago


# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["idUsuario","nombres","apellidos","email","username","pais_usuario","tipo_usuario","con_contrato","rol_consultor"]
    search_fields = ["idUsuario","nombres","apellidos","email","username","pais_usuario","tipo_usuario","con_contrato","rol_consultor"]
    list_filter = ["pais_usuario","tipo_usuario","con_contrato","rol_consultor"]
    list_editable = ["pais_usuario","tipo_usuario","con_contrato","rol_consultor"]


class SolicitudProductoAdmin(admin.ModelAdmin):
    list_display = ["idSolicitud","user","nombreProducto","categoria","cantidadKG","fechaSolicitud","estadoSolicitud"]
    search_fields = ["idSolicitud","user__nombres","user__apellidos","categoria__nombre","cantidadKG","estadoSolicitud"]
    list_filter = ["categoria","fechaSolicitud","estadoSolicitud"]
    list_editable = ["categoria","estadoSolicitud"]


class SubastaProductoAdmin(admin.ModelAdmin):
    list_display = ["idSubasta","user","nombreProducto","categoria","cantidadKG","precioSubasta","fechaSubasta","estadoSubasta"]
    search_fields = ["idSubasta","user__nombres","user__apellidos","categoria__nombre","cantidadKG","precioSubasta","fechaSubasta","estadoSubasta"]
    list_filter = ["cantidadKG","precioSubasta","categoria","fechaSubasta","estadoSubasta"]
    list_editable = ["categoria","estadoSubasta"]


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["idProducto","idProductor","idCliente","nombre","categoria","precioKilo","cantidadKG","fechaPublicacion","estadoPago"]
    search_fields = ["idProducto","idProductor__nombres","idProductor__apellidos","idCliente__nombres","idCliente__apellidos",
                    "nombre","categoria__nombre","precioKilo","cantidadKG","fechaPublicacion","estadoPago"]
    list_filter = ["idProductor","idCliente","nombre","categoria","precioKilo","cantidadKG","fechaPublicacion","estadoPago"]
    list_editable = ["idProductor","idCliente","estadoPago"]
    

class TransporteProductoAdmin(admin.ModelAdmin):
    list_display = ["user","nombreProducto","categoria","nombreEmpresa","tipoTransporte","dimensionTransporte","refrigeracionTransporte",
    "capacidadCarga","precioTransporte","estadoTransporte","fechaTransporte","fechaEstimada"]
    search_fields = ["user__nombres","user__apellidos","nombreProducto","categoria__nombre","nombreEmpresa","tipoTransporte","precioTransporte"]
    list_filter = ["categoria","tipoTransporte","dimensionTransporte","refrigeracionTransporte","capacidadCarga","precioTransporte","estadoTransporte"]
    list_editable = ["precioTransporte","fechaEstimada","estadoTransporte"]
    
class PagoAdmin(admin.ModelAdmin):
    list_display = ["idUsuario","idProducto","fechaPago","pagado"]
    search_fields = ["idUsuario__nombres","idUsuario__apellidos","idProducto__nombre","fechaPago","pagado"]
    list_filter = ["idUsuario__nombres","idUsuario__apellidos","idProducto__nombre","fechaPago","pagado"]
    list_editable = []


admin.site.register(Producto,ProductoAdmin)
admin.site.register(User,UsuarioAdmin)
admin.site.register(Categoria)
admin.site.register(SubastaProducto,SubastaProductoAdmin)
admin.site.register(SolicitudProducto,SolicitudProductoAdmin)
admin.site.register(TransporteProducto,TransporteProductoAdmin)
admin.site.register(Pago,PagoAdmin)