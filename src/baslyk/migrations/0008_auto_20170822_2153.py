# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0007_auto_20170822_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 22, 21, 53, 19, 540419, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='vehicle_condition',
            field=models.CharField(max_length=20, null=True, choices=[(b'Running', b'Running'), (b"Doesn't run", b"Doesn't run")]),
        ),
    ]
