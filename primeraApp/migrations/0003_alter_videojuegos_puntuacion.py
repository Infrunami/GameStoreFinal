# Generated by Django 4.1.3 on 2022-11-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0002_remove_videojuegos_id_juego_videojuegos_puntuacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuegos',
            name='puntuacion',
            field=models.CharField(default='', max_length=2),
        ),
    ]