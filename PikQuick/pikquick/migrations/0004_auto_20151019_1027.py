# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0003_auto_20151019_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='desc1',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='desc2',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='img2',
        ),
    ]
