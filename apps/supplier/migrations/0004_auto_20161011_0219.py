# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_auto_20161010_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierproduct',
            name='supplier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_supplierproduct_supplier', to='supplier.Supplier'),
        ),
        migrations.AlterField(
            model_name='suppliersubsidiary',
            name='supplier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_suppliersubsidiary_supplier', to='supplier.Supplier'),
        ),
    ]