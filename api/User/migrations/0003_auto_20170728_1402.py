# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20170728_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.EmailField(max_length=100),
        ),
    ]