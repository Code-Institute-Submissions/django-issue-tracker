# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-18 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20180917_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='screenshot',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]