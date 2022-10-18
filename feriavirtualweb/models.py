from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid 
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

ROL_USUARIO = (
    ("COMPRADOR", "Comprador"),
    ("VENDEDOR", "Vendedor"),
    ("TRANSPORTISTA", "Transportista"),
)

CONTRATO_USUARIO = (
    ("SI", "Si"),
    ("NO", "No"),
) 

PAIS_USUARIO = (
    ("CHILE", "Chile"),
    ("ARGENTINA", "Argentina"),
    ("BRASIL", "Brasil"),
    ("URUGUAY", "Uruguay"),
    ("CHINA", "China"),
    ("PARAGUAY", "Paraguay"),
    ("ESTADOS UNIDOS", "Estados Unidos"),
    ("JAPÓN", "Japón"),
    ("ALEMANIA", "Alemania"),
    ("ESPAÑA", "España"),
    ("FRANCIA", "Francia"),
    ("PORTUGAL", "Portugal"),
)

class User(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de Usuario',unique= True, max_length=100)
    email = models.EmailField(max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length= 200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length= 200, blank = True, null = True)
    pais_usuario = models.CharField(max_length=15,choices=PAIS_USUARIO,default=" ")
    tipo_usuario = models.CharField(max_length=15,choices=ROL_USUARIO,default=" ")
    con_contrato = models.CharField(max_length=2,choices=CONTRATO_USUARIO,default=" ")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

class Categoria(models.Model):
	"""Model representing a Categoria."""
	nombre = models.CharField(max_length=50)

	class Meta:
		ordering = ['nombre']

	def get_absolute_url(self):
		return reverse('categoria-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.nombre

    

    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    precioKilo = models.DecimalField(max_digits = 5, decimal_places = 2)
    descripcion = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.URLField('URL de Imagen',max_length=300, default='',null=True, blank=True)
    stock = models.IntegerField(default=0,verbose_name = 'Stock')

    class Meta:
        ordering=['nombre']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombre
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Producto."""
        return reverse('producto-detail', args=[str(self.idProducto)])    



class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=False)
    idProducto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=False)
    precioKilo = models.DecimalField(max_digits = 5, decimal_places = 2)
    peso = models.DecimalField(max_digits = 5, decimal_places = 2)
    fecha = models.DateTimeField(null=True)


