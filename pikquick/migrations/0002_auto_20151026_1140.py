# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='entrada',
        ),
        migrations.AddField(
            model_name='entrada',
            name='desc1',
            field=models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 1'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='desc2',
            field=models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 2'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='img1',
            field=models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='img2',
            field=models.FileField(default=b'null', upload_to=b'img_public', verbose_name='Imagen de portada'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
