from django import forms
from . models import Producto,Categoria,User

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

    class Meta:
        model = Producto
        fields = ('nombre','categoria','precioKilo','descripcion', 'image',)


