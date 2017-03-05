# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bprs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField()),
                ('item_02', models.PositiveSmallIntegerField()),
                ('item_03', models.PositiveSmallIntegerField()),
                ('item_04', models.PositiveSmallIntegerField()),
                ('item_05', models.PositiveSmallIntegerField()),
                ('item_06', models.PositiveSmallIntegerField()),
                ('item_07', models.PositiveSmallIntegerField()),
                ('item_08', models.PositiveSmallIntegerField()),
                ('item_09', models.PositiveSmallIntegerField()),
                ('item_10', models.PositiveSmallIntegerField()),
                ('item_11', models.PositiveSmallIntegerField()),
                ('item_12', models.PositiveSmallIntegerField()),
                ('item_13', models.PositiveSmallIntegerField()),
                ('item_14', models.PositiveSmallIntegerField()),
                ('item_15', models.PositiveSmallIntegerField()),
                ('item_16', models.PositiveSmallIntegerField()),
                ('item_17', models.PositiveSmallIntegerField()),
                ('item_18', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'BPRS',
                'verbose_name_plural': 'Escalas BPRS',
            },
        ),
        migrations.CreateModel(
            name='Cgi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cgi_a', models.PositiveSmallIntegerField()),
                ('cgi_b', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'escala CGI',
                'verbose_name_plural': 'escalas CGI',
            },
        ),
        migrations.CreateModel(
            name='Eeag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('eeag', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'escala EEAG',
                'verbose_name_plural': 'escalas EEAG',
            },
        ),
        migrations.CreateModel(
            name='Hdrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField()),
                ('item_02', models.PositiveSmallIntegerField()),
                ('item_03', models.PositiveSmallIntegerField()),
                ('item_04', models.PositiveSmallIntegerField()),
                ('item_05', models.PositiveSmallIntegerField()),
                ('item_06', models.PositiveSmallIntegerField()),
                ('item_07', models.PositiveSmallIntegerField()),
                ('item_08', models.PositiveSmallIntegerField()),
                ('item_09', models.PositiveSmallIntegerField()),
                ('item_10', models.PositiveSmallIntegerField()),
                ('item_11', models.PositiveSmallIntegerField()),
                ('item_12', models.PositiveSmallIntegerField()),
                ('item_13', models.PositiveSmallIntegerField()),
                ('item_14', models.PositiveSmallIntegerField()),
                ('item_15', models.PositiveSmallIntegerField()),
                ('item_16', models.PositiveSmallIntegerField()),
                ('item_17', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'escala Hamilton',
                'verbose_name_plural': 'escalas Hamilton',
            },
        ),
        migrations.CreateModel(
            name='Identificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Panss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_p01', models.PositiveSmallIntegerField()),
                ('item_p02', models.PositiveSmallIntegerField()),
                ('item_p03', models.PositiveSmallIntegerField()),
                ('item_p04', models.PositiveSmallIntegerField()),
                ('item_p05', models.PositiveSmallIntegerField()),
                ('item_p06', models.PositiveSmallIntegerField()),
                ('item_p07', models.PositiveSmallIntegerField()),
                ('item_n01', models.PositiveSmallIntegerField()),
                ('item_n02', models.PositiveSmallIntegerField()),
                ('item_n03', models.PositiveSmallIntegerField()),
                ('item_n04', models.PositiveSmallIntegerField()),
                ('item_n05', models.PositiveSmallIntegerField()),
                ('item_n06', models.PositiveSmallIntegerField()),
                ('item_n07', models.PositiveSmallIntegerField()),
                ('item_g01', models.PositiveSmallIntegerField()),
                ('item_g02', models.PositiveSmallIntegerField()),
                ('item_g03', models.PositiveSmallIntegerField()),
                ('item_g04', models.PositiveSmallIntegerField()),
                ('item_g05', models.PositiveSmallIntegerField()),
                ('item_g06', models.PositiveSmallIntegerField()),
                ('item_g07', models.PositiveSmallIntegerField()),
                ('item_g08', models.PositiveSmallIntegerField()),
                ('item_g09', models.PositiveSmallIntegerField()),
                ('item_g10', models.PositiveSmallIntegerField()),
                ('item_g11', models.PositiveSmallIntegerField()),
                ('item_g12', models.PositiveSmallIntegerField()),
                ('item_g13', models.PositiveSmallIntegerField()),
                ('item_g14', models.PositiveSmallIntegerField()),
                ('item_g15', models.PositiveSmallIntegerField()),
                ('item_g16', models.PositiveSmallIntegerField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'PANSS',
                'verbose_name_plural': 'Escalas PANSS',
            },
        ),
        migrations.CreateModel(
            name='Plutchik_s',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.BooleanField()),
                ('item_02', models.BooleanField()),
                ('item_03', models.BooleanField()),
                ('item_04', models.BooleanField()),
                ('item_05', models.BooleanField()),
                ('item_06', models.BooleanField()),
                ('item_07', models.BooleanField()),
                ('item_08', models.BooleanField()),
                ('item_09', models.BooleanField()),
                ('item_10', models.BooleanField()),
                ('item_11', models.BooleanField()),
                ('item_12', models.BooleanField()),
                ('item_13', models.BooleanField()),
                ('item_14', models.BooleanField()),
                ('item_15', models.BooleanField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'Escala de Riesgo Suicida de Plutchik',
            },
        ),
        migrations.CreateModel(
            name='Plutchik_v',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField()),
                ('item_02', models.PositiveSmallIntegerField()),
                ('item_03', models.PositiveSmallIntegerField()),
                ('item_04', models.PositiveSmallIntegerField()),
                ('item_05', models.PositiveSmallIntegerField()),
                ('item_06', models.PositiveSmallIntegerField()),
                ('item_07', models.PositiveSmallIntegerField()),
                ('item_08', models.PositiveSmallIntegerField()),
                ('item_09', models.PositiveSmallIntegerField()),
                ('item_10', models.PositiveSmallIntegerField()),
                ('item_11', models.PositiveSmallIntegerField()),
                ('item_12', models.BooleanField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'Escala de Riesgo Violencia de Plutchik',
            },
        ),
        migrations.CreateModel(
            name='Satisfaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_1', models.PositiveSmallIntegerField()),
                ('item_2', models.PositiveSmallIntegerField()),
                ('item_3', models.PositiveSmallIntegerField()),
                ('item_4', models.PositiveSmallIntegerField()),
                ('item_5', models.PositiveSmallIntegerField()),
                ('item_6', models.PositiveSmallIntegerField()),
                ('item_7', models.PositiveSmallIntegerField()),
                ('item_8', models.PositiveSmallIntegerField()),
                ('item_9', models.TextField()),
                ('item_10', models.TextField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'Escala Satisfacción',
                'verbose_name_plural': 'Escalas Satisfacción',
            },
        ),
        migrations.CreateModel(
            name='Who_das',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('test', models.PositiveSmallIntegerField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'escala WHO-DAS',
                'verbose_name_plural': 'escalas WHO-DAS',
            },
        ),
        migrations.CreateModel(
            name='Ymrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('item_01', models.PositiveSmallIntegerField()),
                ('item_02', models.PositiveSmallIntegerField()),
                ('item_03', models.PositiveSmallIntegerField()),
                ('item_04', models.PositiveSmallIntegerField()),
                ('item_05', models.PositiveSmallIntegerField()),
                ('item_06', models.PositiveSmallIntegerField()),
                ('item_07', models.PositiveSmallIntegerField()),
                ('item_08', models.PositiveSmallIntegerField()),
                ('item_09', models.PositiveSmallIntegerField()),
                ('item_10', models.PositiveSmallIntegerField()),
                ('item_11', models.PositiveSmallIntegerField()),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'escala Young de manía',
                'verbose_name_plural': 'escalas Young de manía',
            },
        ),
        migrations.AddField(
            model_name='hdrs',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
        migrations.AddField(
            model_name='eeag',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
        migrations.AddField(
            model_name='cgi',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
        migrations.AddField(
            model_name='bprs',
            name='identificador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador'),
        ),
    ]
