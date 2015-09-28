# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Todas las Publicaciones"
        ordering = ['-fecha']

    usuario = models.CharField(u'Usuario', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    img1 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    img2 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    desc1 = models.TextField(u'Descripcion Imagen 1' , max_length = 100 , default='')
    desc2 = models.TextField(u'Descripcion Imagen 2' , max_length = 100 , default='')
    descPub = models.TextField(u'Descripcion de la Publicacion' , max_length = 100 , default='Cual')
    published = models.BooleanField(u'¿Publicado?', default=True)

    def __str__(self):
        return self.usuario.encode('utf8') + " / "+self.descPub.encode('utf8')

class Coment(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    postDelComent = models.ForeignKey(Entrada)
    fecha = models.DateTimeField(u'Fecha del comentario',auto_now_add=True)

    def __str__(self):
        return "Nombre: "+self.nombre.encode('utf8')+" / Mensaje: "+self.mensaje.encode('utf8')
