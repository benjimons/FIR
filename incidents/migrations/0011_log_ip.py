# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-08 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0010_auto_20170122_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='ip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
