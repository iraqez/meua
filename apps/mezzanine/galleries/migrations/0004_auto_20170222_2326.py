# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_auto_20170212_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='content_en',
            new_name='content_uk_UA',
        ),
        migrations.RenameField(
            model_name='galleryimage',
            old_name='description_en',
            new_name='description_uk_UA',
        ),
    ]
