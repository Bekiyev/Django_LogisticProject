# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baslyk', '0014_contactus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='Contact',
        ),
    ]
