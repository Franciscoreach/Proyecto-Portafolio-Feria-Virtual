# Generated by Django 4.1.1 on 2022-10-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualweb', '0002_producto_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]