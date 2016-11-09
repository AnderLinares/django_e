# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0006_auto_20161023_2045'),
        ('core', '0028_auto_20161023_1424'),
        ('vehicle', '0009_auto_20161023_2205'),
        ('product', '0006_auto_20161023_1918'),
        ('customer', '0005_auto_20161024_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActDeliveryVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('code_adv_taller', models.CharField(blank=True, max_length=200, null=True)),
                ('service_taller', models.CharField(choices=[('MAINTENANCE', 'Maintenance'), ('SERVICE', 'Service')], default='MAINTENANCE', max_length=20)),
                ('type_solicitude_entry', models.CharField(choices=[('ENTRY', 'Entry'), ('EXIT', 'Exit')], max_length=20)),
                ('type_solicitude_exit', models.CharField(choices=[('ENTRY', 'Entry'), ('EXIT', 'Exit')], max_length=20)),
                ('km_exit', models.PositiveSmallIntegerField(default=0)),
                ('km_entry', models.PositiveSmallIntegerField(default=0)),
                ('following_maintenance', models.DateField(blank=True, default='', null=True)),
                ('fuel_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_fuel_entry', to='core.VehicleFuel')),
                ('fuel_exit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_fuel_exit', to='core.VehicleFuel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_person', to='core.Person')),
                ('taxi_driver_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_taxi_driver_entry', to='core.Person')),
                ('taxi_driver_exit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_taxi_driver_exit', to='core.Person')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_actdeliveryvehicle_vehicle', to='vehicle.Vehicle')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InventoryDeliveryVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('act_delivery_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_inventorydeliveryvehicle_act_delivery_vehicle', to='taller.ActDeliveryVehicle')),
                ('vehicle_inventory_entry', models.ManyToManyField(blank=True, related_name='taller_inventorydeliveryvehicle_vehicle_inventory_entry', to='core.VehicleInventory')),
                ('vehicle_inventory_exit', models.ManyToManyField(blank=True, related_name='taller_inventorydeliveryvehicle_vehicle_inventory_exit', to='core.VehicleInventory')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ObservationDeliveryVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('observation_inspection', models.TextField(blank=True, null=True)),
                ('observation_evaluation', models.TextField(blank=True, null=True)),
                ('observation_correction', models.TextField(blank=True, null=True)),
                ('observation_conclusion', models.TextField(blank=True, null=True)),
                ('act_delivery_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_observationdeliveryvehicle_act_delivery_vehicle', to='taller.ActDeliveryVehicle')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstore_applicant', to='customer.UserProfile')),
                ('subsidiary', models.ManyToManyField(related_name='taller_purchaseorderstore_subsidiary', to='company.Subsidiary')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderStoreDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('observation', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstoredetail_product', to='product.Product')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstoredetail_product_category', to='product.ProductCategory')),
                ('product_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstoredetail_product_subcategory', to='product.ProductSubCategory')),
                ('purchase_order_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstoredetail_purchase_order_store', to='taller.PurchaseOrderStore')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taller_purchaseorderstoredetail_vehicle', to='vehicle.Vehicle')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='labour',
            unique_together=set([('name',)]),
        ),
    ]
