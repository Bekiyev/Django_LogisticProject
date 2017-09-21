# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0012_auto_20170822_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='vehicle_condition',
            field=models.CharField(max_length=20, null=True, choices=[(b'Runs', b'Runs'), (b"Doesn't run", b"Doesn't run")]),
        ),
    ]
