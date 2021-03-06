# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('team', '0004_auto_20161006_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('current_status', models.CharField(choices=[('', '--Choose--'), ('ENABLED', 'Enabled'), ('DISABLED', 'Disabled')], default='ENABLED', max_length=10)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_groupmodule_group', to='auth.Group')),
                ('module', models.ManyToManyField(related_name='team_groupmodule_module', to='team.Module')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='group',
        ),
        migrations.RemoveField(
            model_name='team',
            name='module',
        ),
        migrations.RemoveField(
            model_name='teammodule',
            name='module',
        ),
        migrations.RemoveField(
            model_name='teammodule',
            name='team',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamModule',
        ),
    ]
