# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0007_auto_20150928_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='usuario',
            field=models.CharField(default=b'', max_length=100, verbose_name='Usuario'),
        ),
    ]
