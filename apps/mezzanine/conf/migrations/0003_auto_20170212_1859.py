# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('conf', '0002_auto_20170212_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='site',
        ),
        migrations.AddField(
            model_name='setting',
            name='site',
            field=models.ManyToManyField(editable=False, to='sites.Site'),
        ),
    ]
