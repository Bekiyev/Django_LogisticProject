# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0005_auto_20170822_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='EstimatedShippingDate',
            new_name='Estimated_Shipping_Date',
        ),
    ]
