# Generated by Django 4.2.1 on 2023-05-25 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contol_estudios', '0002_remove_estudiante_dni_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='profesion',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='telefono',
        ),
    ]