from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import AbstractUser, BaseUserManager



# Create your models here.


ROL_USUARIO = (
    ("COMPRADOR", "Comprador"),
    ("VENDEDOR", "Vendedor"),
    ("DISTRIBUIDOR", "Distribuidor"),
)

class User(AbstractUser):
    tipo_usuario = models.CharField(max_length=12,choices=ROL_USUARIO,default="-")

class Region(models.Model):
	"""Model representing a Region."""
	nombre = models.CharField(max_length=100)

	class Meta:
		ordering = ['nombre']

	def get_absolute_url(self):
		return reverse('region-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.nombre
		


        
class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    propietario = models.CharField(max_length=200)
    precio = models.IntegerField(null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=False)
    url = models.URLField(max_length=300, default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    

    class Meta:
        ordering=['nombre']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombre
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Producto."""
        return reverse('producto-detail', args=[str(self.id)])