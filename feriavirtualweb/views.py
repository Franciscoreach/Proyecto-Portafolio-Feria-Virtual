from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Producto,Categoria,User,SolicitudProducto,SubastaProducto
from django.db.models import Q, query
from . forms import ProductoForm, CustomUserCreationForm,SolicitudForm,SubastaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
#Importación de Mensajes
from django.contrib import messages
#Importaciones Correo
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import json

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def productos(request):
    num_productos=Producto.objects.all()
    return render(
        request,
        'productos.html',
        context={'num_productos':num_productos},
    )


def todolosproductos(request):
    num_productos=Producto.objects.all()
    return render(
        request,
        'allproductos.html',
        context={'num_productos':num_productos},
    )


def conversaciones(request):

    return render(
        request,
        'conversacion.html',
        context={},
    )


def noticias(request):
    return render(
        request,
        'noticias.html',
        context={},
    )

def nosotros(request):
    return render(
        request,
        'nosotros.html',
        context={},
    )

def solicitudes(request):
    num_solicitudes=SolicitudProducto.objects.all()
    return render(
        request,
        'solicitudes.html',
        context={'num_solicitudes':num_solicitudes},
    )

def subastas(request):
    num_subastas=SubastaProducto.objects.all()
    return render(
        request,
        'subastas.html',
        context={'num_subastas':num_subastas},
    )

def perfilUsuario(request):
    num_subastas=SubastaProducto.objects.all()
    num_solicitudes=SolicitudProducto.objects.all()
    return render(
        request,
        'perfilusuario.html',
        context={'num_subastas':num_subastas,'num_solicitudes':num_solicitudes},
    )    

#Vista Creada para Correo
def send_email(mail):
    context = {'mail': mail}


    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Solicitud Contacto Soporte Feria Virtual',
        'CodigoFacilito',
        settings.EMAIL_HOST_USER,
        [mail]
        # , cc = ['virtual.feria.empresa@gmail.com']

    )

    email.attach_alternative(content, 'text/html')
    email.send()    

def contacto(request): 
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email(mail)
        messages.success(request, "Correo enviado correctamente")
        #Redirigir al Home
        return redirect(to="index")
    return render( request, 'contacto.html',context={},)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
            password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redirigir al Home
            return redirect(to="index")
        data["form"] = formulario 

    return render(request,'registration/registro.html',data)

    

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic


#Crud de Producto

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')
    
class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductoListView(generic.ListView):
    model = Producto
    template_name = 'templates/feriavirtualweb/producto_list.html'
    queryset = Producto.objects.all()

    paginate_by = 10

#-------------------Compra de Productos/ Working ----------------------

# class ListadoProductoDisponible(generic.ListView):
#     model = Producto
#     paginate_by = 9
#     template_name = 'disponible_producto_list.html'
    

#     def get_queryset(self):
#         queryset = self.model.objects.filter(stock__gte = 1)
#         return queryset

# class DetalleProductoDisponible(generic.DetailView):
#     model = Producto
#     template_name = 'detalle_disponible_producto.html'


# class RegistrarCompra(CreateView):
#     model = Reserva
#     success_url = reverse_lazy('producto:listar_productos_disponibles')
    
#     #ERROR EN REQUEST AJAX

#     def post (self, request, *args, **kwargs):
#         if request.is_ajax():
#             print(request.POST)
#         return HttpResponse('')


#-------------------Fin Compra de Productos -----------------------------

#Crear y Listar Solicitudes
class SolicitudDetailView(generic.DetailView):
    model = SolicitudProducto

class SolicitudListView(generic.ListView):
    model = SolicitudProducto
    template_name = 'templates/feriavirtualweb/solicitudproducto_list.html'
    queryset = SolicitudProducto.objects.all()

    paginate_by = 10

def solicitud_new(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #Conseguir ID Usuario Logeado
            post.user = request.user
            post.save()
            #form.save_m2m()
            messages.success(request, "¡Tú solicitud se ha ingresado correctamente!")
            #Redirigir a la Solicitud
            return redirect('solicitud-detail', pk=post.pk)
    else:
        form = SolicitudForm()
        return render(request, 'feriavirtualweb/solicitud_form.html', {'form': form})

#Crear y Listar Subastas

class SubastaDetailView(generic.DetailView):
    model = SubastaProducto

class SubastaListView(generic.ListView):
    model = SubastaProducto
    template_name = 'templates/feriavirtualweb/subastaproducto_list.html'
    queryset = SubastaProducto.objects.all()

    paginate_by = 10

def subasta_new(request):
    if request.method == "POST":
        form = SubastaForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #Conseguir ID Usuario Logeado
            post.user = request.user
            post.save()
            #form.save_m2m()
            messages.success(request, "¡Tú solicitud para Subar un Producto se ha ingresado correctamente!")
            #Redirigir al detalle de la Subasta
            return redirect('subasta-detail', pk=post.pk)
    else:
        form = SubastaForm()
        return render(request, 'feriavirtualweb/subasta_form.html', {'form': form})




def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #Conseguir ID Usuario Logeado
            post.user = request.user
            post.save()
            #form.save_m2m()
            return redirect('producto-detail', pk=post.pk)
    else:
        form = ProductoForm()
        return render(request, 'feriavirtualweb/producto_form.html', {'form': form})

def producto_edit(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('producto-detail', pk=post.pk)
    else:
        form = ProductoForm(instance=post)
    return render(request, 'feriavirtualweb/producto_form.html', {'form': form})

