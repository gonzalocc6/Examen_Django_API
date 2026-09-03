from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    anio_publicacion = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('devuelto', 'Devuelto'),
        ('retrasado', 'Retrasado'),
    ]

    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestamos')

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.usuario.username}"
