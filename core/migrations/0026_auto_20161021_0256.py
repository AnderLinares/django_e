# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 02:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20161021_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxconfiguration',
            old_name='code',
            new_name='value',
        ),
        migrations.AlterUniqueTogether(
            name='taxconfiguration',
            unique_together=set([('name',)]),
        ),
    ]
