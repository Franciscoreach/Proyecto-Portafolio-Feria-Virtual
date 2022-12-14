# Generated by Django 4.1.1 on 2022-10-24 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualweb', '0005_alter_producto_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudProducto',
            fields=[
                ('idSolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50)),
                ('cantidadKG', models.IntegerField(default=0, verbose_name='Cantidad de Kilos')),
                ('estadoSolicitud', models.CharField(choices=[('EN PROCESO', 'En Proceso'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada')], default='En Proceso', max_length=15)),
                ('fechaSolicitud', models.DateField(auto_now=True, verbose_name='Fecha Publicacion')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feriavirtualweb.categoria')),
            ],
            options={
                'verbose_name': 'SolicitudProducto',
                'verbose_name_plural': 'SolicitudProducto',
            },
        ),
        migrations.CreateModel(
            name='SubastaProducto',
            fields=[
                ('idSubasta', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50)),
                ('cantidadKG', models.IntegerField(default=0, verbose_name='Cantidad de Kilos')),
                ('precioSubasta', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estadoSubasta', models.CharField(choices=[('EN PROCESO', 'En Proceso'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada')], default='En Proceso', max_length=15)),
                ('fechaSubasta', models.DateField(auto_now=True, verbose_name='Fecha Publicacion')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feriavirtualweb.categoria')),
            ],
            options={
                'verbose_name': 'SubastaProducto',
                'verbose_name_plural': 'SubastaProductos',
            },
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='user',
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidadKG',
            field=models.IntegerField(default=0, verbose_name='Cantidad de Kilos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fechaPublicacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Publicacion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='idCliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ID_Cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='producto',
            name='idProductor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ID_Productor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.CharField(choices=[('PRODUCTOR', 'Productor'), ('CLIENTE', 'Cliente'), ('TRANSPORTISTA', 'Transportista')], default=' ', max_length=15),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.AddField(
            model_name='subastaproducto',
            name='idUsuario',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudproducto',
            name='idUsuario',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
