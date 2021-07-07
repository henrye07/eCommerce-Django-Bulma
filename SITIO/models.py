from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length=200,null=False, unique=True)
    def __str__(self):
        return f"{self.categoria}"

class Productos(models.Model):
    title=models.CharField(max_length=250, null=False, blank=False)
    image=models.FileField(upload_to='imagenes/', blank=False)
    description=models.CharField(max_length=5000,null=False, blank=False)
    price=models.FloatField(max_length=3,null=False, blank=False)
    categoria_pertenece=models.ForeignKey(Categorias,on_delete=models.CASCADE,null=False, blank=False)

    def __str__(self):
        return '{} {}'.format(self.title , self.categoria_pertenece)
