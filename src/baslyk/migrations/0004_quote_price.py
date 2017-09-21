# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0003_auto_20170822_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='Price',
            field=models.IntegerField(max_length=100, null=True, blank=True),
        ),
    ]
