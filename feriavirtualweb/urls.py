from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('productos/', views.productos, name='productos'),
    path('conversaciones/', views.conversaciones, name='conversaciones'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
    path('todolosproductos/', views.todolosproductos, name='todolosproductos'),
    path('miperfil/', views.perfilUsuario, name='miperfil'),
    #Productos
    path('productoslista/', views.ProductoListView.as_view(), name='productoslista'),
    path('producto/<str:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    #Registro 
    path('registro/',views.registro,name="registro"),
    #URL Disponibilidad Producto
    #path('listado-productos-disponibles/',views.ListadoProductoDisponible.as_view(),name="listado_productos_disponibles"),
    #path('detalle-producto-disponible/<str:pk>',views.DetalleProductoDisponible.as_view(),name="detalle_producto_disponible"),
    #path('reservar-compra/',views.RegistrarCompra.as_view(), name = 'reservar_compra')
    #Solicitudes
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/<str:pk>', views.SolicitudDetailView.as_view(), name='solicitud-detail'),
    path('solicitudlista/', views.SolicitudListView.as_view(), name='solicitudlista'),
    #Subastas
    path('subastas/', views.subastas, name='subastas'),
    path('subasta/<str:pk>', views.SubastaDetailView.as_view(), name='subasta-detail'),
    path('subastalista/', views.SubastaListView.as_view(), name='subastalista'),
]

urlpatterns += [
    #Producto CRUD
    path('producto/create/', views.producto_new,name='producto_create'),
    path('producto/<str:pk>/update/', views.producto_edit, name='producto_update'),
    path('producto/<str:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
    #Solicitud Create
    path('solicitud/create/', views.solicitud_new,name='solicitud_create'),
    #Subasta Create
    path('subasta/create/', views.subasta_new,name='subasta_create'),
]