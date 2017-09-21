# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0008_auto_20170822_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_estimate',
            field=models.DecimalField(default=775.87, max_digits=50, decimal_places=20),
            preserve_default=False,
        ),
    ]
