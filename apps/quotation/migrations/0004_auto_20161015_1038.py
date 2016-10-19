# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20161009_1155'),
        ('supplier', '0010_auto_20161013_0023'),
        ('core', '0024_auto_20161008_1358'),
        ('quotation', '0003_auto_20161015_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('igv_tax', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('total_paid', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('date', models.DateField()),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstore_exchange_rate', to='core.Currency')),
                ('exchange_rate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstore_exchange_rate', to='core.ExchangeRate')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstore_vehicle', to='supplier.Supplier')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='QuotationStoreDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('amount_price', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstoredetail_product', to='product.Product')),
                ('quotation_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationstoredetail_quotation_supplier', to='quotation.QuotationStore')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='quotationsupplier',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='quotationsupplier',
            name='exchange_rate',
        ),
        migrations.RemoveField(
            model_name='quotationsupplier',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='quotationsupplierdetail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='quotationsupplierdetail',
            name='quotation_supplier',
        ),
        migrations.DeleteModel(
            name='QuotationSupplier',
        ),
        migrations.DeleteModel(
            name='QuotationSupplierDetail',
        ),
    ]
