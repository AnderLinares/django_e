# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20161008_1358'),
        ('supplier', '0010_auto_20161013_0023'),
        ('product', '0004_auto_20161009_1155'),
        ('quotation', '0002_auto_20161006_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('igv_tax', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('total_paid', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('date', models.DateField()),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationsupplier_exchange_rate', to='core.Currency')),
                ('exchange_rate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationsupplier_exchange_rate', to='core.ExchangeRate')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationsupplier_vehicle', to='supplier.Supplier')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='QuotationSupplierDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('amount_price', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationsupplierdetail_product', to='product.Product')),
                ('quotation_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationsupplierdetail_quotation_supplier', to='quotation.QuotationSupplier')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='quotationmaintenancedetail',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='quotationmaintenancedetail',
            name='product_subcategory',
        ),
    ]