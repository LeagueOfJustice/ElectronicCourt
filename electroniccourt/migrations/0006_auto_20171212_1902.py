# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electroniccourt', '0005_auto_20171212_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='electroniccourt.Role'),
        ),
    ]
