# Generated by Django 4.1.1 on 2022-10-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feriavirtualweb', '0007_rename_idusuario_solicitudproducto_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subastaproducto',
            old_name='idUsuario',
            new_name='user',
        ),
    ]