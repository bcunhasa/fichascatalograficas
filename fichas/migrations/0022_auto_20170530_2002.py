# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0021_auto_20170529_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='anexos',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
