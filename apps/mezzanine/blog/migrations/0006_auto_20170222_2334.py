# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170222_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='title_uk_UA',
            new_name='title_uk',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='_meta_title_uk_UA',
            new_name='_meta_title_uk',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='content_uk_UA',
            new_name='content_uk',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='description_uk_UA',
            new_name='description_uk',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='title_uk_UA',
            new_name='title_uk',
        ),
    ]
