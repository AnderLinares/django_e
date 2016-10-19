# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20161005_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('is_principal', models.BooleanField(default=False)),
            ],
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together=set([('name',)]),
        ),
    ]