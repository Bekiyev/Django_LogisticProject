# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0002_auto_20170822_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='EstimatedShippingDate',
            field=models.CharField(max_length=100, choices=[(b'ASAP', b'ASAP'), (b'Within 2 Weeks', b'Within 2 Weeks'), (b'Within 30 Days', b'Within 30 Days'), (b'Not Sure', b'Not Sure')]),
        ),
    ]
