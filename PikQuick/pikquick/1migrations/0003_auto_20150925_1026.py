# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0002_auto_20150925_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='user',
            new_name='usuario',
        ),
    ]
