# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0004_auto_20170814_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apellido',
            new_name='carne',
        ),
    ]