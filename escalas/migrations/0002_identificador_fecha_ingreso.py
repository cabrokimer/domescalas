# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificador',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]