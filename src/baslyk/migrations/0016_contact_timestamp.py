# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0015_auto_20170823_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 5, 52, 50, 274457, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
