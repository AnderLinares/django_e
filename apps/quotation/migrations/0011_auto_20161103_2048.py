# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotation', '0010_auto_20161016_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationmaintenance',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='quotationmaintenance',
            name='exchange_rate',
        ),
        migrations.RemoveField(
            model_name='quotationmaintenancedetail',
            name='product',
        ),
        migrations.AddField(
            model_name='quotationmaintenance',
            name='applicant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='quotation_quotationmaintenance_applicant', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotationmaintenance',
            name='code_qt_maintenance',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]