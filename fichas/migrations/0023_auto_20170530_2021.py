# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0022_auto_20170530_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='nome',
            field=models.CharField(default='', max_length=200),
        ),
    ]
