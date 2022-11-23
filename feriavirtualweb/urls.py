from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required #Para Proteger rutas 

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
    path('todolosproductos/', login_required(views.todolosproductos), name='todolosproductos'),
    path('listar-usuarios/', views.UsuarioListPDF.as_view(), name='usuario_all'),
    #Productos
    path('productoslista/', login_required(views.ProductoListView.as_view()), name='productoslista'),
    path('producto/<str:pk>', login_required(views.ProductoDetailView.as_view()), name='producto-detail'),
    path('listar-productos/', views.ProductoListPDF.as_view(), name='producto_all'),
    #Registro 
    path('registro/',views.registro,name="registro"),
    #Solicitudes
    path('solicitudes/', login_required(views.solicitudes), name='solicitudes'),
    path('solicitud/<str:pk>', login_required(views.SolicitudDetailView.as_view()), name='solicitud-detail'),
    path('solicitudlista/', login_required(views.SolicitudListView.as_view()), name='solicitudlista'),
    path('listar-solicitudes/', views.SolicitudListPDF.as_view(), name='solicitud_all'),
    #Subastas
    path('subastas/', login_required(views.subastas), name='subastas'),
    path('subasta/<str:pk>', login_required(views.SubastaDetailView.as_view()), name='subasta-detail'),
    path('subastalista/', login_required(views.SubastaListView.as_view()), name='subastalista'),
    path('listar-subastas/', views.SubastaListPDF.as_view(), name='subasta_all'),
    #Stripe
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', login_required(views.success_view), name='success'),
    path('cancel/', login_required(views.cancel_view), name='cancel'),
    #Pagos
    path('pagoslista/', login_required(views.PagoListView.as_view()), name='pagoslista'),
    path('pago/<str:pk>', login_required(views.PagoDetailView.as_view()), name='pago-detail'),
    path('listar-pagos/', views.PagoListPDF.as_view(), name='pago_all'),
    #Transportista
    path('transporteproductos-lista/', login_required(views.transporteproductos_lista), name='transporteproductos-lista'),
    path('transportes/', login_required(views.transportes), name='transportes'),
    path('transporte/<str:pk>', login_required(views.TransporteDetailView.as_view()), name='transportesubasta-detail'),
    path('transportelista/', login_required(views.TransporteListView.as_view()), name='transportelista'),
    path('listar-transportistas/', views.TrasnportistaListPDF.as_view(), name='transportista_all'),
    #Estados Producto Transportista
    path('transporteEstadoF/<str:pk>', views.transporteEstadoF.as_view(), name='transporteEstadoFinalizado'),
    path('transporteEstadoD/<str:pk>', views.transporteEstadoD.as_view(), name='transporteEstadoDespachado'),
]

urlpatterns += [
    #Producto CRUD
    path('producto/create/', login_required(views.producto_new),name='producto_create'),
    path('producto/<str:pk>/update/', login_required(views.producto_edit), name='producto_update'),
    path('producto/<str:pk>/delete/', login_required(views.ProductoDelete.as_view()), name='producto_delete'),
    #Solicitud Create
    path('solicitud/create/', login_required(views.solicitud_new),name='solicitud_create'),
    #Subasta Create
    path('subasta/create/', login_required(views.subasta_new),name='subasta_create'),
    #Transporte Create
    path('transporte/create/', login_required(views.transporte_new),name='transporte_create'),
]