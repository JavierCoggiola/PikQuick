# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'pikquick.views.inicio', name='inicio'),
                       url(r'^usuario/nuevo$','pikquick.views.nuevo_usuario', name='nuevo_usuario'),
                       url(r'^usuario/ingreso$','pikquick.views.ingreso_usuario', name='ingreso_usuario'),
                       url(r'^usuario/salir$','pikquick.views.salir_usuario', name='salir_usuario'),
                       url(r'^usuario/cambiar_pass$','pikquick.views.cambiar_pass', name='cambiar_pass'),
                       url(r'^perfil/(?P<usuario>\w+)/$', 'pikquick.views.perfil', name='perfil'),
                       url(r'^nuevapublic$','pikquick.views.nuevapublic', name='nuevapublic'),
                       url(r'^crear_public/$','pikquick.views.crear_public', name='crear_public'),
                       url(r'^save_message/$', 'pikquick.views.save_message', name='save_message'),
                       url(r'^ver_message/$', 'pikquick.views.ver_message', name='ver_message'),
                       url(r'^ajustes/$', 'pikquick.views.ajustes', name='ajustes'),
                       url(r'^deletePost/$', 'pikquick.views.deletePost', name='deletePost'),
                       url(r'^noSeguir/(?P<toUnFollow_un>\w+)/$', 'pikquick.views.unFollow', name='unFollow'),
                       url(r'^seguir/(?P<toFollow_un>\w+)/$', 'pikquick.views.follow', name='follow'),
                       url(r'^todo/$', 'pikquick.views.inicioAll', name='inicioAll'),
                       url(r'^buscador/(?P<busqueda>\w+)/$', 'pikquick.views.buscador', name='buscador'),
                      )
