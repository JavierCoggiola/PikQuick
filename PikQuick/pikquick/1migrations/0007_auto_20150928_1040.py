# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pikquick', '0006_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coment',
            old_name='postDelComent',
            new_name='entrada',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='mensaje',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='nombre',
        ),
        migrations.AddField(
            model_name='coment',
            name='coment_txt',
            field=models.TextField(default=datetime.datetime(2015, 9, 28, 13, 39, 49, 366204, tzinfo=utc), max_length=100, verbose_name=b'Comentatrio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coment',
            name='fecha_pub',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 13, 40, 40, 756405, tzinfo=utc), verbose_name=b'date published', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coment',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
    ]
