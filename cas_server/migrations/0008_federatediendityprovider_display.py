# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas_server', '0007_auto_20160704_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='federatediendityprovider',
            name='display',
            field=models.BooleanField(default=True, help_text='Display the provider on the login page', verbose_name='display'),
        ),
    ]
