# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0010_auto_20170822_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_estimate',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=2, blank=True),
        ),
    ]
