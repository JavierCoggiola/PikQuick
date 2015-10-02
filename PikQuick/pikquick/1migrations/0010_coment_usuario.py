# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0009_remove_coment_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='usuario',
            field=models.CharField(default=b' ', max_length=100, verbose_name='Usuario'),
        ),
    ]
