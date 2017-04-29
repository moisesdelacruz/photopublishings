# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('themes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themes.Theme'),
        ),
    ]