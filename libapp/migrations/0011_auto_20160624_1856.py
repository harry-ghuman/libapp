# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import libapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0010_auto_20160624_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='pubyr',
            field=models.IntegerField(blank=True, null=True, validators=[libapp.models.clean_fields]),
        ),
    ]
