from django import forms
from . models import Producto,Categoria,User,SolicitudProducto,SubastaProducto,TransporteProducto

from django.contrib.auth.forms import UserCreationForm


#Contenido de Formulario Para Registrarse en Sitio Web
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"nombres","apellidos","pais_usuario","tipo_usuario","con_contrato","email","password1","password2",]

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    idCliente = forms.ModelChoiceField(queryset=User.objects.all(), label='Nombre del Cliente',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    idProductor = forms.ModelChoiceField(queryset=User.objects.all(), label='Nombre del Productor',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    idTransportista = forms.ModelChoiceField(queryset=User.objects.all(), label='Nombre del Transportista',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    precioKilo = forms.IntegerField(label='Precio por Kilo del Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción del Producto', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    image = forms.ImageField(label='Imagen del Producto',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    cantidadKG = forms.IntegerField(label='Cantidad de Kilos del Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    stripe_product_id = forms.CharField(label='Ingresa el ID del Pago del Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precioTransporte = forms.IntegerField(label='Precio del Transporte del Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))


    class Meta:
        model = Producto
        fields = ('nombre','idCliente','idProductor','idTransportista','categoria','precioKilo','descripcion', 'image','cantidadKG','stripe_product_id','precioTransporte')


class SolicitudForm(forms.ModelForm):

    nombreProducto = forms.CharField(label='Nombre del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    cantidadKG = forms.IntegerField(label='Cantidad de KG a Solicitar', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = SolicitudProducto
        fields = ('nombreProducto','categoria','cantidadKG')

class SubastaForm(forms.ModelForm):
    nombreProducto = forms.CharField(label='Nombre del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    cantidadKG = forms.IntegerField(label='Cantidad de KG para el Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precioSubasta = forms.IntegerField(label='Precio a Ofrecer para el Producto (Dolares)', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = SubastaProducto
        fields = ('nombreProducto','categoria','cantidadKG','precioSubasta')


REFRIGERACION = (
    ("SI", "Si"),
    ("NO", "No"),
)

DIMENSION_TRANSPORTE = (
    ("GRANDE", "Grande"),
    ("MEDIANO", "Mediano"),
    ("PEQUEÑO", "Pequeño"),
)

TIPO_TRANSPORTE = (
    ("AVION", "Avion"),
    ("CAMION", "Camion"),
    ("BARCO", "Barco"),
    ("OTRO", "Otro"),
)


ESTADO_TRANSPORTE = (
    ("PENDIENTE", "Pendiente"),
    ("ACEPTADO", "Aceptado"),
    ("RECHAZADO", "Rechazado"),
    ("EN PROCESO", "En Proceso"),
    ("DESPACHADO", "Despachado"),
    ("FINALIZADO", "Finalizado"),
)


class TransporteSubastaForm(forms.ModelForm):
    nombreProducto = forms.CharField(label='Nombre del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
    ))
    nombreEmpresa = forms.CharField(label='Nombre de la Empresa a Cargo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    tipoTransporte = forms.ChoiceField(label='Tipo de Transporte',choices=TIPO_TRANSPORTE,
            widget=forms.Select(
            attrs={
            'class':'form-control'
        }        
    ))
    dimensionTransporte = forms.ChoiceField(label='Dimension del Transporte',choices=DIMENSION_TRANSPORTE,
            widget=forms.Select(
            attrs={
            'class':'form-control'
        }        
    ))
    refrigeracionTransporte = forms.ChoiceField(label='Refrigeración del Transporte',choices=REFRIGERACION,
            widget=forms.Select(
            attrs={
            'class':'form-control'
        }        
    ))
    capacidadCarga = forms.IntegerField(label='Capacidad de Carga del Transporte (KG)', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precioTransporte = forms.IntegerField(label='Precio a Ofrecer para el Transporte del Producto (Dolares)', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    fechaEstimada = forms.DateField(label='Fecha Estimada de Entrega del Producto (Dia/Mes/Año)', widget=forms.DateInput(format='%d/%m/%Y',
        attrs={
            'placeholder': '__/__/____',
            'class':'form-control'
        }
    ))
    

    class Meta:
        model = TransporteProducto
        fields = ('nombreProducto','categoria','nombreEmpresa','tipoTransporte','dimensionTransporte','refrigeracionTransporte','capacidadCarga',
        'precioTransporte','fechaEstimada')