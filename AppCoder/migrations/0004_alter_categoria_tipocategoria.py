# Generated by Django 4.1 on 2022-09-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_categoria_posiciontrabajo_trabajocompas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='tipocategoria',
            field=models.IntegerField(),
        ),
    ]
