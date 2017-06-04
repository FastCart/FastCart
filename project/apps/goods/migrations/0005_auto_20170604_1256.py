# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_lastgoods_is_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]