from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Producto,Categoria,User
from django.db.models import Q, query
from . forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
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

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
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
