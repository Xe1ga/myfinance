# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import table.models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20170829_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='date_buy',
            field=models.DateField(default=table.models.getnow, help_text='гггг-мм-дд', verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date_income',
            field=models.DateField(),
        ),
    ]
