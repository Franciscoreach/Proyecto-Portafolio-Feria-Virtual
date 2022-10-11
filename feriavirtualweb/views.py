from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Producto, Region
from django.db.models import Q, query
from . forms import RegionForm, ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
import json

# Create your views here.
def index(request):

    return render(
        request,
        'index.html',
        context={},
    )

def productos(request):

    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains == busqueda) |
            Q(propietario_icontains == busqueda)
        ).distinct()


    return render(
        request,
        'productos.html',
        context={},
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

def contacto(request):
    return render(
        request,
        'contacto.html',
        context={},
    )

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


class RegionDelete(DeleteView):
    model = Region
    success_url = reverse_lazy('index')


class RegionDetailView(generic.DetailView):
    model = Region
    
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')
    
class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductoListView(generic.ListView):
    model = Producto
    template_name = 'templates/agrired/producto_list.html'
    queryset = Producto.objects.all()

    paginate_by = 10



def region_new(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('region-detail', pk=post.pk)
    else:
        form = RegionForm()
        return render(request, 'agrired/region_form.html', {'form': form})

def region_edit(request, pk):
    post = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('region-detail', pk=post.pk)
    else:
        form = RegionForm(instance=post)
    return render(request, 'agrired/region_form.html', {'form': form})

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
        return render(request, 'agrired/producto_form.html', {'form': form})

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
    return render(request, 'agrired/producto_form.html', {'form': form})