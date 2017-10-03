# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-03 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0074_auto_20171003_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificador',
            name='estado_alta',
            field=models.CharField(blank=True, choices=[(b'mejor', b'Mejor\xc3\xada'), (b'ind', b'Indicaci\xc3\xb3n'), (b'peor', b'Emperoamiento de s\xc3\xadntomas'), (b'clau', b'Claudicaci\xc3\xb3n cuidador'), (b'litic', b'Ideacion autolitica'), (b'agit', b'Agitacion')], max_length=4, null=True, verbose_name=b'Motivo alta'),
        ),
    ]