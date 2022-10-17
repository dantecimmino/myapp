from django.db import models
from django.contrib.auth.forms import User



# Create your models here.

class PaletasPadel(models.Model):

    def __str__(self):
        return f'paletas {self.nombre}'

    nombre = models.CharField(max_length=80)
    material = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    forma= models.CharField(max_length=80)
    precio = models.IntegerField()
    imagen= models.ImageField(upload_to='paletas', null=True)

class Pelotas(models.Model):

    def __str__(self):
        return f'Pelotas {self.marca}'

    marca = models.CharField(max_length=80)
    precio = models.IntegerField()
    imagen= models.ImageField(upload_to='pelotas', null=True)


class Avatar(models.Model):

    def __str__(self):
        return f'Avatar {self.user}'

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Avatarimagenes(models.Model):

    def __str__(self):
        return f'Avatar img {self.user}'

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

