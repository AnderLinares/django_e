# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20161006_1228'),
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationmaintenance',
            name='vehicle_plaque',
        ),
        migrations.AddField(
            model_name='quotationmaintenance',
            name='vehicle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationmaintenance_vehicle', to='vehicle.Vehicle'),
            preserve_default=False,
        ),
    ]