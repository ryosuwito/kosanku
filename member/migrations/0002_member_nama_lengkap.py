# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nama_lengkap',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
