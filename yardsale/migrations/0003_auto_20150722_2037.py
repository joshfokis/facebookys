# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import yardsale.models


class Migration(migrations.Migration):

    dependencies = [
        ('yardsale', '0002_auto_20150722_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='warning',
            name='image2',
            field=models.ImageField(upload_to=yardsale.models.get_image_path, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='warning',
            name='image3',
            field=models.ImageField(upload_to=yardsale.models.get_image_path, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='warning',
            name='image4',
            field=models.ImageField(upload_to=yardsale.models.get_image_path, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='warning',
            name='image5',
            field=models.ImageField(upload_to=yardsale.models.get_image_path, blank=True, null=True),
        ),
    ]
