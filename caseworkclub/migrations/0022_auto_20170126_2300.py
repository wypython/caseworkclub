# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-26 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caseworkclub', '0021_auto_20170125_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casenote',
            options={'ordering': ['-timestamp']},
        ),
    ]
