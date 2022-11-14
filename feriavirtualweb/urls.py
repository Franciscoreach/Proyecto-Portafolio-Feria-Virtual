from django.urls import path
from . import views

urlpatterns = [
    #General
    path('',views.index,name='index'),
    path('productos/', views.productos, name='productos'),
    path('conversaciones/', views.conversaciones, name='conversaciones'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
    #Usuario
    path('miperfil/', views.perfilUsuario, name='miperfil'),
    path('todolosproductos/', views.todolosproductos, name='todolosproductos'),
    path('listar-usuarios/', views.UsuarioListPDF.as_view(), name='usuario_all'),
    #Productos
    path('productoslista/', views.ProductoListView.as_view(), name='productoslista'),
    path('producto/<str:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('listar-productos/', views.ProductoListPDF.as_view(), name='producto_all'),
    #Registro 
    path('registro/',views.registro,name="registro"),
    #Solicitudes
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitud/<str:pk>', views.SolicitudDetailView.as_view(), name='solicitud-detail'),
    path('solicitudlista/', views.SolicitudListView.as_view(), name='solicitudlista'),
    path('listar-solicitudes/', views.SolicitudListPDF.as_view(), name='solicitud_all'),
    #Subastas
    path('subastas/', views.subastas, name='subastas'),
    path('subasta/<str:pk>', views.SubastaDetailView.as_view(), name='subasta-detail'),
    path('subastalista/', views.SubastaListView.as_view(), name='subastalista'),
    path('listar-subastas/', views.SubastaListPDF.as_view(), name='subasta_all'),
    #Stripe
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
    #Pagos
    path('pagoslista/', views.PagoListView.as_view(), name='pagoslista'),
    path('pago/<str:pk>', views.PagoDetailView.as_view(), name='pago-detail'),
    path('listar-pagos/', views.PagoListPDF.as_view(), name='pago_all'),
    #Transportista
    path('transporteproductos-lista/', views.transporteproductos_lista, name='transporteproductos-lista'),
    path('transportes/', views.transportes, name='transportes'),
    path('transporte/<str:pk>', views.TransporteDetailView.as_view(), name='transportesubasta-detail'),
    path('transportelista/', views.TransporteListView.as_view(), name='transportelista'),
    path('listar-transportistas/', views.TrasnportistaListPDF.as_view(), name='transportista_all'),


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
    #Transporte Create
    path('transporte/create/', views.transporte_new,name='transporte_create'),
]