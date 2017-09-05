# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import table.models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20170809_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='date_buy',
            field=models.DateTimeField(default=table.models.getnow, help_text='гггг-мм-дд', verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='typeofbuy',
            name='typeofbuy_text',
            field=models.CharField(max_length=200, verbose_name='Тип расхода'),
        ),
    ]
