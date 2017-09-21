# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0004_quote_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='Price',
            new_name='Quote_Estimate',
        ),
    ]
