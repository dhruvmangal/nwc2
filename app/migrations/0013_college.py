# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-03 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('registration_date', models.DateField(verbose_name='registration date')),
            ],
        ),
    ]
