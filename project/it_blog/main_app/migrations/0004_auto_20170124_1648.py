# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
