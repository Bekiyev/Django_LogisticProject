# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('Running', models.BooleanField()),
                ('Email', models.EmailField(max_length=254)),
                ('EstimatedShippingDate', models.CharField(max_length=10, choices=[(b'ASAP', b'ASAP'), (b'Within 2 Weeks', b'Within 2 Weeks'), (b'Within 30 Days', b'Within 30 Days'), (b'Not Sure', b'Not Sure')])),
            ],
        ),
    ]
