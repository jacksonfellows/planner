# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
