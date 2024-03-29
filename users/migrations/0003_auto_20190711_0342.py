# Generated by Django 2.0.13 on 2019-07-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_encuesta_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='apellido_materno',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='apellido_paterno',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='rut',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
