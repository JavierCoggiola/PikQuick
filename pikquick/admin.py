# -*- coding: utf-8 -*-
from django.contrib import admin
from pikquick.models import Entrada, Coment, Follow #, Imagen

# Register your models here.
admin.site.register(Entrada)
admin.site.register(Coment)
admin.site.register(Follow)
#admin.site.register(Imagen)
