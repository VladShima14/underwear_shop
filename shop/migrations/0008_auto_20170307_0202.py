# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170307_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookbookpage',
            name='links',
        ),
        migrations.AddField(
            model_name='lookbookpage',
            name='type',
            field=models.CharField(db_index=True, default='portrait', max_length=100),
        ),
    ]
