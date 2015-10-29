# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'pikquick.views.inicio', name='inicio'),
                       url(r'^usuario/nuevo$','pikquick.views.nuevo_usuario', name='nuevo_usuario'),
                       url(r'^usuario/ingreso$','pikquick.views.ingreso_usuario', name='ingreso_usuario'),
                       url(r'^usuario/salir$','pikquick.views.salir_usuario', name='salir_usuario'),
                       url(r'^usuario/cambiar_pass$','pikquick.views.cambiar_pass', name='cambiar_pass'),
                       url(r'^perfil$', 'pikquick.views.perfil', name='perfil'),
                       url(r'^nuevapublic$','pikquick.views.nuevapublic', name='nuevapublic'),
                       url(r'^crear_public/$','pikquick.views.crear_public', name='crear_public'),
                       url(r'^save_message/$', 'pikquick.views.save_message', name='save_message'),
                       url(r'^ver_message/$', 'pikquick.views.ver_message', name='ver_message'),
                       url(r'^user_profile/(?P<username>\w+)/$', 'pikquick.views.user_profile', name='user_profile'),
                       url(r'^deletePost/$', 'pikquick.views.deletePost', name='deletePost'),
                      )
