# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0005_auto_20150928_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='published',
        ),
        migrations.AlterField(
            model_name='entrada',
            name='desc1',
            field=models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 1'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='desc2',
            field=models.TextField(default=b'', max_length=100, verbose_name='Descripcion Imagen 2'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='descPub',
            field=models.TextField(default=b'Help', max_length=100, verbose_name='Descripcion de la Publicacion'),
        ),
    ]
