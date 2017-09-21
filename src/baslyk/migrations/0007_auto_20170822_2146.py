# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0006_auto_20170822_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='From',
            new_name='departure_location',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Make',
            new_name='destination_location',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Estimated_Shipping_Date',
            new_name='estimated_shipping_date',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Quote_Estimate',
            new_name='quote_estimate',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='Model',
            new_name='vehicle_make',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='To',
            new_name='vehicle_model',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='Running',
        ),
        migrations.AddField(
            model_name='quote',
            name='vehicle_condition',
            field=models.CharField(max_length=5, null=True, choices=[(b'Running', b'Running'), (b"Doesn't run", b"Doesn't run")]),
        ),
    ]
