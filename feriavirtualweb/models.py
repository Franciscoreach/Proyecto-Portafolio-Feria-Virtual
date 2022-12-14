from django.db import models
from django.conf import settings
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid 
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

ROL_USUARIO = (
    ("PRODUCTOR", "Productor"),
    ("CLIENTE", "Cliente"),
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

ROL_ESPECIAL = (
    ("NO", "No"),
    ("SI", "Si"),
) 

#Rol_consultor // Solo puede ser otorgado por algún administrador en el panel de administrador


class User(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de Usuario',unique= True, max_length=100)
    email = models.EmailField(max_length=254,unique = True)
    nombres = models.CharField('Nombres', max_length= 200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length= 200, blank = True, null = True)
    pais_usuario = models.CharField(max_length=15,choices=PAIS_USUARIO,default=" ")
    tipo_usuario = models.CharField(max_length=15,choices=ROL_USUARIO,default=" ")
    con_contrato = models.CharField('Con contrato (en caso de ser cliente, favor seleccionar "no")',max_length=2,choices=CONTRATO_USUARIO,default=" ")
    rol_consultor = models.CharField(max_length=2,choices=ROL_ESPECIAL,default="NO")


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres',"apellidos",'email']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this User."""
        return reverse('usuer-detail', args=[str(self.idUsuario)]) 

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

    
#Creación de Modelo para Crear Solicitudes de Producto
# 
ESTADO_SOLICITUD = (
    ("EN PROCESO", "En Proceso"),
    ("ACEPTADA", "Aceptada"),
    ("RECHAZADA", "Rechazada"),
)

class SolicitudProducto(models.Model):
    idSolicitud = models.AutoField(primary_key= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1")
    nombreProducto = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    cantidadKG = models.IntegerField(default=0,verbose_name = 'Cantidad de Kilos')
    estadoSolicitud = models.CharField(max_length=15,choices=ESTADO_SOLICITUD,default="EN PROCESO")
    fechaSolicitud = models.DateField('Fecha Publicacion', auto_now= True, auto_now_add= False) 

    
    class Meta:
        
        verbose_name = 'SolicitudProducto'
        verbose_name_plural = 'SolicitudProducto'
        
        
    def __str__(self):
        """String for representing the Model object."""
        return self.nombreProducto


ESTADO_SUBASTA = (
    ("EN PROCESO", "En Proceso"),
    ("ACEPTADA", "Aceptada"),
    ("RECHAZADA", "Rechazada"),
)


#Creación de Modelo para la Subasta de los Productos
# 
class SubastaProducto(models.Model):
    idSubasta = models.AutoField(primary_key= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1")
    nombreProducto = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    cantidadKG = models.IntegerField(default=0,verbose_name = 'Cantidad de Kilos')
    precioSubasta = models.DecimalField(max_digits = 6, decimal_places = 2)
    estadoSubasta = models.CharField(max_length=15,choices=ESTADO_SUBASTA,default="EN PROCESO")
    fechaSubasta = models.DateField('Fecha Publicacion', auto_now= True, auto_now_add= False) 

    
    class Meta:
        
        verbose_name = 'SubastaProducto'
        verbose_name_plural = 'SubastaProductos'
        
        
    def __str__(self):
        """String for representing the Model object."""
        return self.nombreProducto


#Adición Campos idProductor/idCliente/fechaPublicacion/cantidadKG
# 

#Creación de Modelo para la Despachar los Productos por los Transportistas
# 

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



class TransporteProducto(models.Model):
    idTransporte = models.AutoField(primary_key= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1")
    nombreProducto = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    nombreEmpresa = models.CharField(max_length=50)
    tipoTransporte = models.CharField(max_length=15,choices=TIPO_TRANSPORTE,default="OTRO")
    dimensionTransporte = models.CharField(max_length=15,choices=DIMENSION_TRANSPORTE,default="MEDIANO")
    refrigeracionTransporte = models.CharField(max_length=15,choices=REFRIGERACION,default="NO")
    capacidadCarga = models.IntegerField(default=0,verbose_name = 'Capacidad de Carga')
    precioTransporte = models.DecimalField(max_digits = 6, decimal_places = 2)
    estadoTransporte = models.CharField(max_length=15,choices=ESTADO_TRANSPORTE,default="PENDIENTE")
    fechaTransporte = models.DateField('Fecha Publicacion', auto_now= True, auto_now_add= False) 
    fechaEstimada = models.DateField('Fecha Estimada de Entrega',null=True, blank=False) 
    
    class Meta:
        
        verbose_name = 'TransporteProducto'
        verbose_name_plural = 'TransporteProductos'
        
        
    def __str__(self):
        """String for representing the Model object."""
        return self.nombreProducto



ESTADO_PAGO = (
    ("PENDIENTE", "Pendiente"),
    ("PAGADO", "Pagado"),
    ("EXPIRADO", "Expirado"),
)

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=False,related_name='ID_Cliente')
    idProductor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=False,related_name='ID_Productor')
    idTransportista = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=False,related_name='ID_Transportista')
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    precioKilo = models.DecimalField(max_digits = 6, decimal_places = 2)
    descripcion = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    cantidadKG = models.IntegerField(default=0,verbose_name = 'Cantidad de Kilos')
    fechaPublicacion = models.DateField('Fecha Publicacion', auto_now= True, auto_now_add= False)
    estadoPago = models.CharField(max_length=15,choices=ESTADO_PAGO,default="PENDIENTE")
    stripe_product_id = models.CharField(max_length=100, null=True, blank=True)
    precioTransporte = models.DecimalField(max_digits = 6, decimal_places = 2, null=True, blank=False)

    class Meta:
        ordering=['nombre']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombre
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Producto."""
        return reverse('producto-detail', args=[str(self.idProducto)])    



class Pago(models.Model):
    idUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1")
    idProducto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=False)
    fechaPago = models.DateField('Fecha Pago Producto', auto_now= True, auto_now_add= False)
    pagado = models.BooleanField(default=False)



