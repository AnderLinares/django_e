# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0003_auto_20161019_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='discount_tax',
            new_name='igv_total',
        ),
    ]
