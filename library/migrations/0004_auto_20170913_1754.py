# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-13 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170913_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_extra',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=6),
        ),
    ]