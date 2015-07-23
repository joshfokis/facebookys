# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yardsale', '0003_auto_20150722_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.NullBooleanField(default=True),
        ),
    ]
