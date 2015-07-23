# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yardsale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='edited_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='warning',
            name='editor',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='warning',
            name='publish_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
