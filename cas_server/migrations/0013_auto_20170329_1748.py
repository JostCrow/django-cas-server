# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas_server', '0012_auto_20170328_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
