# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('team', '0005_auto_20161006_1947'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmodule',
            unique_together=set([('group',)]),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set([('name',)]),
        ),
    ]