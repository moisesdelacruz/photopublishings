# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170429_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
    ]
