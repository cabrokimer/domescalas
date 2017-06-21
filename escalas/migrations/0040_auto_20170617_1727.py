# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escalas', '0039_auto_20170617_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icg_ge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('icg_ge', models.PositiveSmallIntegerField(null=True)),
                ('quien_ge', models.CharField(max_length=3, null=True)),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'escala ICG_Gravedad',
                'verbose_name_plural': 'escalas ICG_Gravedad',
            },
        ),
        migrations.CreateModel(
            name='Icg_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('icg_me', models.PositiveSmallIntegerField(null=True)),
                ('quien_me', models.CharField(max_length=3, null=True)),
                ('identificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalas.Identificador')),
            ],
            options={
                'verbose_name': 'escala ICG_Mejoría',
                'verbose_name_plural': 'escalas ICG_Mejoría',
            },
        ),
        migrations.RemoveField(
            model_name='icg',
            name='identificador',
        ),
        migrations.DeleteModel(
            name='Icg',
        ),
    ]