# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20180805_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='alamat_lengkap',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]