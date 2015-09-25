# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0003_auto_20150925_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del comentario')),
            ],
        ),
        migrations.AddField(
            model_name='entrada',
            name='descPub',
            field=models.TextField(default=b'\xc2\xbf?', max_length=100, verbose_name='Descripcion de la Publicacion'),
        ),
        migrations.AddField(
            model_name='coment',
            name='postDelComent',
            field=models.ForeignKey(to='pikquick.Entrada'),
        ),
    ]
