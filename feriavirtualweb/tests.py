# Create your tests here.
from django.test import TestCase
from . models import User,Categoria,SolicitudProducto,SubastaProducto,TransporteProducto,Producto,Pago

class UserClienteModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        User.objects.create(idUsuario=1000, username='Tester1',email='tester@gmail.com',nombres='Tester',apellidos='Tester',pais_usuario='CHILE',
        tipo_usuario='CLIENTE',con_contrato='NO',rol_consultor='NO')
    
    def test_username_label(self):
        User=User.objects.get(idUsuario=1000)
        field_label = User._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_email_label(self):
        User=User.objects.get(idUsuario=1000)
        field_label = User._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')
    
    def test_nombres_label(self):
        User=User.objects.get(idUsuario=1000)
        field_label = User._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label,'nombres')

    def test_apellidos_label(self):
        User=User.objects.get(idUsuario=1000)
        field_label = User._meta.get_field('apellidos').verbose_name
        self.assertEquals(field_label,'apellidos')

    def test_username_max_length(self):
        User=User.objects.get(idUsuario=1000)
        max_length = User._meta.get_field('username').max_length
        self.assertEquals(max_length,100)

class UserProductorModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        User.objects.create(idUsuario=1001, username='Tester2',email='tester@gmail.com',nombres='Tester',apellidos='Tester',pais_usuario='CHILE',
        tipo_usuario='PRODUCTOR',con_contrato='SI',rol_consultor='NO')
    
    def test_username_label(self):
        User=User.objects.get(idUsuario=1001)
        field_label = User._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_email_label(self):
        User=User.objects.get(idUsuario=1001)
        field_label = User._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')
    
    def test_nombres_label(self):
        User=User.objects.get(idUsuario=1001)
        field_label = User._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label,'nombres')

    def test_apellidos_label(self):
        User=User.objects.get(idUsuario=1001)
        field_label = User._meta.get_field('apellidos').verbose_name
        self.assertEquals(field_label,'apellidos')

    def test_username_max_length(self):
        User=User.objects.get(idUsuario=1001)
        max_length = User._meta.get_field('username').max_length
        self.assertEquals(max_length,100)

class UserTransportistaModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        User.objects.create(idUsuario=1002, username='Tester3',email='tester@gmail.com',nombres='Tester',apellidos='Tester',pais_usuario='CHILE',
        tipo_usuario='TRANSPORTISTA',con_contrato='NO',rol_consultor='NO')
    
    def test_username_label(self):
        User=User.objects.get(idUsuario=1002)
        field_label = User._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_email_label(self):
        User=User.objects.get(idUsuario=1002)
        field_label = User._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')
    
    def test_nombres_label(self):
        User=User.objects.get(idUsuario=1002)
        field_label = User._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label,'nombres')

    def test_apellidos_label(self):
        User=User.objects.get(idUsuario=1002)
        field_label = User._meta.get_field('apellidos').verbose_name
        self.assertEquals(field_label,'apellidos')

    def test_username_max_length(self):
        User=User.objects.get(idUsuario=1002)
        max_length = User._meta.get_field('username').max_length
        self.assertEquals(max_length,100)

class UserConsultorModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        User.objects.create(idUsuario=1003, username='Tester4',email='tester@gmail.com',nombres='Tester',apellidos='Tester',pais_usuario='CHILE',
        tipo_usuario='CLIENTE',con_contrato='NO',rol_consultor='SI')
    
    def test_username_label(self):
        User=User.objects.get(idUsuario=1003)
        field_label = User._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_email_label(self):
        User=User.objects.get(idUsuario=1003)
        field_label = User._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')
    
    def test_nombres_label(self):
        User=User.objects.get(idUsuario=1003)
        field_label = User._meta.get_field('nombres').verbose_name
        self.assertEquals(field_label,'nombres')

    def test_apellidos_label(self):
        User=User.objects.get(idUsuario=1003)
        field_label = User._meta.get_field('apellidos').verbose_name
        self.assertEquals(field_label,'apellidos')

    def test_username_max_length(self):
        User=User.objects.get(idUsuario=1003)
        max_length = User._meta.get_field('username').max_length
        self.assertEquals(max_length,100)



class CategoriaProductoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Categoria.objects.create(id= 3,nombre = "Verdura")
    
    def test_nombre_label(self):
        Categoria=Categoria.objects.get(id=3)
        field_label = Categoria._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_nombre_max_length(self):
        Categoria=Categoria.objects.get(id=3)
        max_length = Categoria()._meta.get_field('nombre').max_length
        self.assertEquals(max_length,50)



class SolicitudProductoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        SolicitudProducto.objects.create(idSolicitud=1000, user=1000,nombreProducto='Papas Alegres',categoria='Verdura',cantidadKG=10,
        estadoSolicitud='EN PROCESO',fechaSolicitud='22/11/2022')
    
    def test_nombreProducto_label(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        field_label = SolicitudProducto._meta.get_field('nombreProducto').verbose_name
        self.assertEquals(field_label,'nombreProducto')

    def test_categoria_label(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        field_label = SolicitudProducto._meta.get_field('categoria').verbose_name
        self.assertEquals(field_label,'categoria')
    
    def test_cantidadKG_label(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        field_label = SolicitudProducto._meta.get_field('cantidadKG').verbose_name
        self.assertEquals(field_label,'cantidadKG')

    def test_estadoSolicitud_label(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        field_label = SolicitudProducto._meta.get_field('estadoSolicitud').verbose_name
        self.assertEquals(field_label,'estadoSolicitud')

    def test_fechaSolicitud_label(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        field_label = SolicitudProducto._meta.get_field('fechaSolicitud').verbose_name
        self.assertEquals(field_label,'fechaSolicitud')

    def test_nombreProducto_max_length(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        max_length = SolicitudProducto._meta.get_field('nombreProducto').max_length
        self.assertEquals(max_length,50)

    def test_estadoSolicitud_max_length(self):
        SolicitudProducto=SolicitudProducto.objects.get(idSolicitud=1000)
        max_length = SolicitudProducto._meta.get_field('estadoSolicitud').max_length
        self.assertEquals(max_length,15)

class SubastaProductoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        SubastaProducto.objects.create(idSubasta=1000, user=1001,nombreProducto='Papas Alegres',categoria='Verdura',cantidadKG=10,
        precioSubasta=1000,estadoSubasta='EN PROCESO',fechaSubasta='23/11/2022')
    
    def test_nombreProducto_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('nombreProducto').verbose_name
        self.assertEquals(field_label,'nombreProducto')

    def test_categoria_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('categoria').verbose_name
        self.assertEquals(field_label,'categoria')
    
    def test_cantidadKG_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('cantidadKG').verbose_name
        self.assertEquals(field_label,'cantidadKG')
    
    def test_precioSubasta_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('precioSubasta').verbose_name
        self.assertEquals(field_label,'precioSubasta')

    def test_estadoSubasta_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('estadoSubasta').verbose_name
        self.assertEquals(field_label,'estadoSubasta')

    def test_fechaSubasta_label(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        field_label = SubastaProducto._meta.get_field('fechaSubasta').verbose_name
        self.assertEquals(field_label,'fechaSubasta')

    def test_nombreProducto_max_length(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        max_length = SubastaProducto._meta.get_field('nombreProducto').max_length
        self.assertEquals(max_length,50)

    def test_precioSubasta_max_digits(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        max_digits = SubastaProducto._meta.get_field('precioSubasta').max_digits
        self.assertEquals(max_digits,6)

    def test_estadoSubasta_max_length(self):
        SubastaProducto=SubastaProducto.objects.get(idSubasta=1000)
        max_length = SubastaProducto._meta.get_field('estadoSubasta').max_length
        self.assertEquals(max_length,15)

class TransporteProductoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        TransporteProducto.objects.create(idTransporte=1000, user=1002,nombreProducto='Papas Alegres',categoria='Verdura',nombreEmpresa="CEPAM",
        tipoTransporte='CAMION',dimensionTransporte='PEQUEÑO',refrigeracionTransporte='SI',capacidadCarga=50,precioTransporte=300,
        estadoTransporte='PENDIENTE',fechaTransporte='24/11/2022',fechaEstimada='27/11/2022')
    
    def test_nombreProducto_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('nombreProducto').verbose_name
        self.assertEquals(field_label,'nombreProducto')

    def test_categoria_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('categoria').verbose_name
        self.assertEquals(field_label,'categoria')
    
    def test_nombreEmpresa_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('nombreEmpresa').verbose_name
        self.assertEquals(field_label,'nombreEmpresa')
    
    def test_tipoTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('tipoTransporte').verbose_name
        self.assertEquals(field_label,'tipoTransporte')

    def test_dimensionTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('dimensionTransporte').verbose_name
        self.assertEquals(field_label,'dimensionTransporte')

    def test_refrigeracionTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('refrigeracionTransporte').verbose_name
        self.assertEquals(field_label,'refrigeracionTransporte')
    
    def test_capacidadCarga_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('capacidadCarga').verbose_name
        self.assertEquals(field_label,'capacidadCarga')

    def test_precioTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('precioTransporte').verbose_name
        self.assertEquals(field_label,'precioTransporte')

    def test_estadoTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('estadoTransporte').verbose_name
        self.assertEquals(field_label,'estadoTransporte')
    
    def test_fechaTransporte_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('fechaTransporte').verbose_name
        self.assertEquals(field_label,'fechaTransporte')

    def test_fechaEstimada_label(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        field_label = TransporteProducto._meta.get_field('fechaEstimada').verbose_name
        self.assertEquals(field_label,'fechaEstimada')

    def test_nombreProducto_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = TransporteProducto._meta.get_field('nombreProducto').max_length
        self.assertEquals(max_length,50)
    
    def test_nombreEmpresa_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = SubastaProducto._meta.get_field('nombreEmpresa').max_length
        self.assertEquals(max_length,50)
    
    def test_tipoTransporte_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = TransporteProducto._meta.get_field('tipoTransporte').max_length
        self.assertEquals(max_length,15)
    
    def test_dimensionTransporte_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = TransporteProducto._meta.get_field('dimensionTransporte').max_length
        self.assertEquals(max_length,15)
    
    def test_refrigeracionTransporte_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = TransporteProducto._meta.get_field('refrigeracionTransporte').max_length
        self.assertEquals(max_length,15)

    def test_precioTransporte_max_digits(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_digits = TransporteProducto._meta.get_field('precioTransporte').max_digits
        self.assertEquals(max_digits,6)

    def test_estadoTransporte_max_length(self):
        TransporteProducto=TransporteProducto.objects.get(idTransporte=1000)
        max_length = TransporteProducto._meta.get_field('estadoTransporte').max_length
        self.assertEquals(max_length,15)


class ProductoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Producto.objects.create(idProducto=1000, idCliente=1000,idProductor=1001,idTransportista=1002,
        nombre='Papas Alegres',categoria='Verdura',precioKilo=1000,descripcion='Papas Buenisimas',image='/media/images/papaTest.jpg',cantidadKG=10,
        fechaPublicacion='24/11/2022',estadoPago='PENDIENTE',stripe_product_id='price_1M750TJ1GWHoVyS7kMzMNsw4',precioTransporte=300)
    
    def test_nombre_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_categoria_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('categoria').verbose_name
        self.assertEquals(field_label,'categoria')
    
    def test_precioKilo_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('precioKilo').verbose_name
        self.assertEquals(field_label,'precioKilo')
    
    def test_descripcion_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')

    def test_image_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('image').verbose_name
        self.assertEquals(field_label,'image')

    def test_cantidadKG_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('cantidadKG').verbose_name
        self.assertEquals(field_label,'cantidadKG')
    
    def test_fechaPublicacion_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('fechaPublicacion').verbose_name
        self.assertEquals(field_label,'fechaPublicacion')

    def test_stripe_product_id_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('stripe_product_id').verbose_name
        self.assertEquals(field_label,'stripe_product_id')

    def test_precioTransporte_label(self):
        Producto=Producto.objects.get(idProducto=1000)
        field_label = Producto._meta.get_field('precioTransporte').verbose_name
        self.assertEquals(field_label,'precioTransporte')

    def test_nombre_max_length(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_length = Producto._meta.get_field('nombre').max_length
        self.assertEquals(max_length,50)

    def test_precioKilo_max_digits(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_digits = Producto._meta.get_field('precioKilo').max_digits
        self.assertEquals(max_digits,6)
    
    def test_descripcion_max_length(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_length = Producto._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,1000)
    
    def test_estadoPago_max_length(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_length = Producto._meta.get_field('estadoPago').max_length
        self.assertEquals(max_length,15)
    
    def test_stripe_product_id_max_length(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_length = Producto._meta.get_field('stripe_product_id').max_length
        self.assertEquals(max_length,100)

    def test_precioTransporte_max_digits(self):
        Producto=Producto.objects.get(idProducto=1000)
        max_digits = Producto._meta.get_field('precioTransporte').max_digits
        self.assertEquals(max_digits,6)
    
class PagoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Pago.objects.create(idUsuario=1000, idProducto=1000,fechaPago='25/11/2022',pagado=True)
    
    def test_fechaPago_label(self):
        Pago=Pago.objects.get(idUsuario=1000)
        field_label = Pago._meta.get_field('fechaPago').verbose_name
        self.assertEquals(field_label,'fechaPago')

    def test_pagado_label(self):
        Pago=Pago.objects.get(idUsuario=1000)
        field_label = Pago._meta.get_field('pagado').verbose_name
        self.assertEquals(field_label,'pagado')
    
