# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0002_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='desc',
            field=models.TextField(default=b' ', max_length=100, verbose_name='Descripcion Imagen 1'),
        ),
    ]
