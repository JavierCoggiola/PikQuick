# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('descPub', models.TextField(default=b' ', max_length=100, verbose_name='Descripcion de la Publicacion')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Todas las Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow_time', models.DateTimeField(auto_now=True)),
                ('follower', models.ForeignKey(related_name='who_is_followed', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(related_name='who_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada')),
                ('desc', models.TextField(default=b' ', max_length=100, verbose_name='Descripcion Imagen')),
                ('entrada', models.ForeignKey(related_name='imagenes', to='pikquick.Entrada')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.AddField(
            model_name='coment',
            name='entrada',
            field=models.ForeignKey(to='pikquick.Entrada'),
        ),
    ]
