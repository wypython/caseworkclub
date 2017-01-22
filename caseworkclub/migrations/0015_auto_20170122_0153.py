# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 01:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('caseworkclub', '0014_auto_20170122_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_number',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='NUT Membership Numbers have a capital letter and five digits.', regex='[A-Z]\\d{5}')]),
        ),
    ]
