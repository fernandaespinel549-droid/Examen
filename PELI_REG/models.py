from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class peliculas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    genero = models.TextField()
    director = models.TextField()
    creacion = models.DateField(null= True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.titulo} - {self.user}"