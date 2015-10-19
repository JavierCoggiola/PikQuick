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
    #img1 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    #img2 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    #desc1 = models.TextField(u'Descripcion Imagen 1' , max_length = 100 , default='')
    #desc2 = models.TextField(u'Descripcion Imagen 2' , max_length = 100 , default='')
    descPub = models.TextField(u'Descripcion de la Publicacion' , max_length = 100 , default='Help')

    def __str__(self):
        return self.usuario.encode('utf8') + " / "+self.descPub.encode('utf8')

class Imagen (models.Model):
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    img = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    desc = models.TextField(u'Descripcion Imagen' , max_length = 100 , default=' ')
    entrada = models.ForeignKey(Entrada)

    def __str__(self):
       return self.descPub.encode('utf8')

class Coment(models.Model):
    usuario = models.CharField(u'Usuario', max_length = 100, default=' ')
    fecha_pub = models.DateTimeField('date published', auto_now_add=True)
    coment_txt = models.TextField('Comentatrio', max_length=100)
    published = models.BooleanField(u'Publicado?', default=True)
    entrada = models.ForeignKey(Entrada)

    def __str__(self):
        return self.coment_txt.encode('utf8') + self.usuario.encode('utf8')
