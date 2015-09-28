# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='titulo',
        ),
        migrations.AddField(
            model_name='entrada',
            name='user',
            field=models.CharField(default=1, max_length=100, verbose_name='Usuario'),
            preserve_default=False,
        ),
    ]
