# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_auto_20160520_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvd',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
