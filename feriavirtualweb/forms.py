from django import forms
from . models import Region, Producto,User

from django.contrib.auth.forms import UserCreationForm

#Contenido de Formulario Para Registrarse en Sitio Web
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","tipo_usuario","email","password1","password2",]

class RegionForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre de la Región',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Region
        fields = ('nombre',)

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción del Producto', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    propietario = forms.CharField(label='Nombre del Propietario del Producto',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precio = forms.IntegerField(label='Precio del Producto', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Region',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    url = forms.URLField(label='URL', max_length=300,widget=forms.URLInput(
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
        fields = ('nombre','descripcion','propietario','precio','region', 'url', 'image',)


