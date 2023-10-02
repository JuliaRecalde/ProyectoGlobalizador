from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace = models.URLField()
    fecha_publicacion = models.DateTimeField()
    palabra_clave = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
