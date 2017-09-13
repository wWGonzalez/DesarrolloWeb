# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0002_auto_20170807_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificar', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Clientee',
        ),
    ]
