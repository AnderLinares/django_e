# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20161010_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='logo_url',
            new_name='logo_organization',
        ),
    ]
