from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('productos/', views.productos, name='productos'),
    path('conversaciones/', views.conversaciones, name='conversaciones'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
    path('productoslista/', views.ProductoListView.as_view(), name='productoslista'),
    path('producto/<str:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('registro/',views.registro,name="registro"),
]

urlpatterns += [
    path('producto/create/', views.producto_new,name='producto_create'),
    path('producto/<str:pk>/update/', views.producto_edit, name='producto_update'),
    path('producto/<str:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
]