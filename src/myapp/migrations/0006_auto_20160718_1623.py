# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160718_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='superventa',
            new_name='superventas',
        ),
    ]