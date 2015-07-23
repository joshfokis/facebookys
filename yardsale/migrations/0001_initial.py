# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import yardsale.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('follower', models.CharField(max_length=140)),
                ('following', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
                ('descript', models.TextField(max_length=5000)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to=yardsale.models.get_image_path, blank=True)),
                ('WarningType', models.CharField(choices=[('Bumping', 'Bumping'), ('Pet', 'Pet'), ('Business', 'Business'), ('Outside Links', 'Outside Links'), ('Price Undefined', 'Price Undefined'), ('Other', 'Other')], default='Bumping', max_length=15)),
                ('person', models.ForeignKey(related_name='warnings', to='yardsale.Followers')),
            ],
        ),
    ]
