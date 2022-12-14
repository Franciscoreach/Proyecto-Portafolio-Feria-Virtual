# Generated by Django 4.1.1 on 2022-10-19 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualweb', '0003_producto_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precioKilo',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
