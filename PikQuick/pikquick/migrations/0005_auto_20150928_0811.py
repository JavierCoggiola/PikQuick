# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0004_auto_20150925_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='descPub',
            field=models.TextField(default=b'Quien', max_length=100, verbose_name='Descripcion de la Publicacion'),
        ),
    ]
