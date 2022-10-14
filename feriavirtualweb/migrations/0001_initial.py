# Generated by Django 4.1.1 on 2022-10-14 02:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('pais_usuario', models.CharField(choices=[('CHILE', 'Chile'), ('ARGENTINA', 'Argentina'), ('BRASIL', 'Brasil'), ('URUGUAY', 'Uruguay'), ('CHINA', 'China'), ('PARAGUAY', 'Paraguay'), ('ESTADOS UNIDOS', 'Estados Unidos'), ('JAPÓN', 'Japón'), ('ALEMANIA', 'Alemania'), ('ESPAÑA', 'España'), ('FRANCIA', 'Francia'), ('PORTUGAL', 'Portugal')], default=' ', max_length=15)),
                ('tipo_usuario', models.CharField(choices=[('COMPRADOR', 'Comprador'), ('VENDEDOR', 'Vendedor'), ('TRANSPORTISTA', 'Transportista')], default=' ', max_length=15)),
                ('con_contrato', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], default=' ', max_length=2)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precioKilo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descripcion', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feriavirtualweb.categoria')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('precioKilo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha', models.DateTimeField(null=True)),
                ('idProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feriavirtualweb.producto')),
                ('id_Usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
