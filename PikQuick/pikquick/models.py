# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Todas las Publicaciones"
        ordering = ['-fecha']

    titulo = models.CharField(u'Título', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    img1 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    img2 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    desc1 = models.TextField(u'Epigrafe Imagen 1' , max_length = 100 , default='')
    desc2 = models.TextField(u'Epigrafe Imagen 2' , max_length = 100 , default='')
    published = models.BooleanField(u'Publicado?', default=True)

    def __str__(self):
        return self.titulo
