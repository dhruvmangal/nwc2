# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-31 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_jobseeker_jobseeker_creat_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='jobseeker_creat_date',
        ),
    ]
