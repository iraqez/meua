# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20170222_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='content_uk_UA',
            new_name='content_uk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='_meta_title_uk_UA',
            new_name='_meta_title_uk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='content_uk_UA',
            new_name='content_uk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_uk_UA',
            new_name='description_uk',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_uk_UA',
            new_name='title_uk',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='description_uk_UA',
            new_name='description_uk',
        ),
        migrations.RenameField(
            model_name='productoption',
            old_name='name_uk_UA',
            new_name='name_uk',
        ),
        migrations.RenameField(
            model_name='productvariation',
            old_name='option1_uk_UA',
            new_name='option1_uk',
        ),
        migrations.RenameField(
            model_name='productvariation',
            old_name='option2_uk_UA',
            new_name='option2_uk',
        ),
    ]
