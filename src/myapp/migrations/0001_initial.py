# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('autor', models.CharField(max_length=120)),
            ],
        ),
    ]
