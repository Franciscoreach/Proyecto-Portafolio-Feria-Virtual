from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Producto,Categoria,User,SolicitudProducto,SubastaProducto,Pago,TransporteProducto
from django.db.models import Q, query
from . forms import ProductoForm, CustomUserCreationForm,SolicitudForm,SubastaForm,TransporteSubastaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from . utils import render_to_pdf
#Importación de Mensajes
from django.contrib import messages
#Importaciones Correo
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import json

#Importanciones Stripe
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


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

#Vista Creada para Avisar Pago de Producto
def send_email_pago(mail_pago):
    context = {'mail_pago': mail_pago}


    template = get_template('correo_pago.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        '[FeriaVirtual] Pago de producto solicitado ya disponible.',
        'FeriaVirtual',
        settings.EMAIL_HOST_USER,
        [mail_pago]
        # , cc = ['virtual.feria.empresa@gmail.com']

    )

    email.attach_alternative(content, 'text/html')
    email.send()  

def perfilUsuario(request):
    num_subastas=SubastaProducto.objects.all()
    num_solicitudes=SolicitudProducto.objects.all()
    num_pagos = Pago.objects.all()
    num_transportes = TransporteProducto.objects.all()
    total_solicitudes = SolicitudProducto.objects.count()
    total_subastas = SubastaProducto.objects.count()
    total_productos = Producto.objects.count()
    total_usuarios = User.objects.count()
    total_transportes = TransporteProducto.objects.count()
    total_pagos = Pago.objects.count()

    #Aviso Pago de Producto por Correo
    if request.method == 'POST':
        mail_pago = request.POST.get('mail_pago')

        send_email_pago(mail_pago)
        messages.success(request, "¡Correo de aviso enviado correctamente!")
        #Redirigir al Home
        return redirect(to="miperfil")

    return render(
        request,
        'perfilusuario.html',
        context={'num_subastas':num_subastas,
        'num_solicitudes':num_solicitudes,
        'total_solicitudes':total_solicitudes,
        'total_subastas':total_subastas,
        'total_productos':total_productos,
        'total_usuarios':total_usuarios,
        'num_pagos':num_pagos,
        'num_transportes':num_transportes,
        'total_transportes':total_transportes,
        'total_pagos':total_pagos
        },
    )    

#Vista Creada para Correo de Contacto
def send_email(mail):
    context = {'mail': mail}


    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        '[Feria Virtual] Solicitud de Contacto Soporte.',
        'FeriaVirtual',
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

    

from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.views import generic


#Crud de Producto

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')
    


class ProductoListView(generic.ListView):
    model = Producto
    template_name = 'templates/feriavirtualweb/producto_list.html'
    queryset = Producto.objects.all()

    paginate_by = 10

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
        return render(request, 'feriavirtualweb/formularios/solicitud_form.html', {'form': form})


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
            messages.success(request, "¡Tú solicitud para Subastar un Producto se ha ingresado correctamente!")
            #Redirigir al detalle de la Subasta
            return redirect('subasta-detail', pk=post.pk)
    else:
        form = SubastaForm()
        return render(request, 'feriavirtualweb/formularios/subasta_form.html', {'form': form})




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
        return render(request, 'feriavirtualweb/formularios/producto_form.html', {'form': form})

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
    return render(request, 'feriavirtualweb/formularios/producto_form.html', {'form': form})



# Listado de Distintas Tablas/Modelos para ser Descargados/Visualizados en Formato PDF

class SolicitudListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        solicitudes = SolicitudProducto.objects.all()
        data = {
            'solicitudes' : solicitudes
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_solicitudes_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class SubastaListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        subastas = SubastaProducto.objects.all()
        data = {
            'subastas' : subastas
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_subastas_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class ProductoListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        data = {
            'productos' : productos
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_productos_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class UsuarioListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        data = {
            'usuarios' : usuarios
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_usuarios_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class PagoListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        pagos = Pago.objects.all()
        data = {
            'pagos' : pagos
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_pagos_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class TrasnportistaListPDF(generic.View):
    
    def get(self, request, *args, **kwargs):
        transportistas = TransporteProducto.objects.all()
        data = {
            'transportistas' : transportistas
        }
        pdf = render_to_pdf('feriavirtualweb/informes/lista_transportistas_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')




#Vista Creada para Notificar que el producto ya se encuentrado Pagado
def send_email_pagado(mail_pagado):
        context = {'mail_pagado': mail_pagado}
        template = get_template('correo_pagado.html')
        content = template.render(context)

        email = EmailMultiAlternatives(
            '[FeriaVirtual] ¡Tú Producto ya se encuentra pagado! .',
            'FeriaVirtual',
            settings.EMAIL_HOST_USER,
            [mail_pagado]
            # , cc = ['virtual.feria.empresa@gmail.com']

        )
        email.attach_alternative(content, 'text/html')
        email.send() 

#STRIPE

class CreateCheckoutSessionView(generic.View):

    

    def post(self, request, *args, **kwargs):
        producto = Producto.objects.get(idProducto=self.kwargs["pk"])

        pago = Pago.objects.create(idUsuario=request.user,idProducto = producto, pagado = True)
        producto.estadoPago = "PAGADO"
        pago.save()
        producto.save()
        #Aviso del Producto ya Pagado por Correo
        
        mail_pagado = User.objects.get(idUsuario = request.user.idUsuario).email

        send_email_pagado(mail_pagado)
        messages.success(request, "¡Pago realizado correctamente!")

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': producto.stripe_product_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL + '/feriavirtualweb/success/',
            cancel_url=settings.BASE_URL + '/feriavirtualweb/cancel/',
        )


        return redirect(checkout_session.url)

class ProductoDetailView(generic.DetailView):
    model = Producto

    
def success_view(request):

        return render(request, "feriavirtualweb/success.html")

def cancel_view(request):

        return render(request, "feriavirtualweb/cancel.html")



#Procesos para Transportistas


def transportes(request):
    num_transportes=TransporteProducto.objects.all()
    return render(
        request,
        'transportes.html',
        context={'num_transportes':num_transportes},
    )

def transporteproductos_lista(request):
    num_productos=SubastaProducto.objects.all()
    return render(
        request,
        'feriavirtualweb/productotransportista_list.html',
        context={'num_productos':num_productos},
    )


class TransporteDetailView(generic.DetailView):
    model = TransporteProducto

class TransporteListView(generic.ListView):
    model = TransporteProducto
    template_name = 'templates/feriavirtualweb/transporteproducto_list.html'
    queryset = TransporteProducto.objects.all()

    paginate_by = 10

def transporte_new(request):
    if request.method == "POST":
        form = TransporteSubastaForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #Conseguir ID Usuario Logeado
            post.user = request.user
            post.save()
            #form.save_m2m()
            messages.success(request, "¡Tú solicitud para Transportar un Producto se ha ingresado correctamente!")
            #Redirigir al detalle de la Subasta
            return redirect('transportesubasta-detail', pk=post.pk)
    else:
        form = TransporteSubastaForm()
        return render(request, 'feriavirtualweb/formularios/transportesubasta_form.html', {'form': form})



#Detalle de Pago
class PagoDetailView(generic.DetailView):
    model = Pago
    
class PagoListView(generic.ListView):
    model = Pago
    template_name = 'templates/feriavirtualweb/pago_list.html'
    queryset = Pago.objects.all()

    paginate_by = 10