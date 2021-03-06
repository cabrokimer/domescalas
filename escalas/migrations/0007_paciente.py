# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0006_auto_20170607_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnac', models.DateField(blank=True, verbose_name='Fecha de Nac.')),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'Femenino')], max_length=2)),
                ('sector', models.CharField(blank=True, choices=[('1', 'AIS Gracia'), ('2', 'AIS Dreta'), ('3', 'AIS Guinardó')], max_length=1, verbose_name='Sector')),
                ('e_civil', models.CharField(blank=True, choices=[('1', 'Soltero'), ('2', 'Casado'), ('3', 'Pareja estable'), ('4', 'Separado'), ('5', 'Viudo'), ('6', 'Otro')], max_length=1, verbose_name='Estado civil')),
                ('n_hijos', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de hijos')),
                ('laboral', models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Baja temporal'), ('3', 'Sin trabajo actual'), ('4', 'Pensionista'), ('5', 'Nunca ha trabajado'), ('6', 'Desconocido')], max_length=1, verbose_name='Situación laboral')),
                ('estudios', models.CharField(blank=True, choices=[('1', 'Primarios'), ('2', 'Secundarios'), ('3', 'Superiores'), ('4', 'Sin estudios'), ('5', 'Desconocido')], max_length=1, verbose_name='Nivel de estudios')),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
        ),
    ]
