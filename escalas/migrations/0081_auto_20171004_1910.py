# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-04 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0080_auto_20171004_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico_pac',
            name='dg_ppal',
        ),
        migrations.AddField(
            model_name='diagnostico_pac',
            name='dg_principal',
            field=models.BooleanField(default=True, verbose_name=b'Dg Principal'),
        ),
    ]
