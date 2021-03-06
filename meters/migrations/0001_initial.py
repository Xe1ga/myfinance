# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import meters.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetersData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_meter', models.DateField(default=meters.models.getnow, verbose_name='Дата снятия показаний')),
                ('cold_water', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Холодная вода')),
                ('hot_water', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Горячая вода')),
                ('electricity_apartment', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Электричество в квартире')),
                ('electricity_storeroom', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Электричество в подсобном помещении')),
            ],
            options={
                'ordering': ['-date_meter'],
            },
        ),
    ]
