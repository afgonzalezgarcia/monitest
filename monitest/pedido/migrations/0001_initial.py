# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-20 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('amount', models.FloatField(default=0.0)),
                ('status', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(choices=[('Masculino', 'M'), ('Femenino', 'F')], default='Masculino', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
