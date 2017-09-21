# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0011_auto_20170822_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='vehicle_condition',
            field=models.CharField(max_length=20, null=True, choices=[(b'drives', b'drives'), (b'Runs', b"Doesn't run")]),
        ),
    ]
