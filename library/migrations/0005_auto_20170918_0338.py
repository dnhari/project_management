# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-18 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20170913_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_extra',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='user_extra',
            name='lastName',
        ),
    ]
