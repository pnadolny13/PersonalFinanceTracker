# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0002_auto_20170613_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='input',
            name='input_title',
            field=models.CharField(max_length=200),
        ),
    ]
