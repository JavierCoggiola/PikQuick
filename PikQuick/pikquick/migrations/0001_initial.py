# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(default=b' ', max_length=100, verbose_name='Usuario')),
                ('fecha_pub', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('coment_txt', models.TextField(max_length=100, verbose_name=b'Comentatrio')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=100, verbose_name='Usuario')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('img1', models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada')),
                ('img2', models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada')),
                ('desc1', models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 1')),
                ('desc2', models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 2')),
                ('descPub', models.TextField(default=b'Help', max_length=100, verbose_name='Descripcion de la Publicacion')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Todas las Publicaciones',
            },
        ),
        migrations.AddField(
            model_name='coment',
            name='entrada',
            field=models.ForeignKey(to='pikquick.Entrada'),
        ),
    ]
