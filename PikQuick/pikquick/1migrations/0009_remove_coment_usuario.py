# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0008_coment_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coment',
            name='usuario',
        ),
    ]
