# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entities',
            new_name='Entity',
        ),
    ]
