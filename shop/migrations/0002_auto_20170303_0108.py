# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение меню'),
        ),
    ]
