# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristic',
            field=models.TextField(blank=True, verbose_name='Состав товара'),
        ),
    ]
