# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='Running',
            field=models.CharField(max_length=5, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
