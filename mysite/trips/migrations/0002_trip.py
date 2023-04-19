# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('updated', models.DateTimeField(auto_created=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('trip_title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('airplane', models.CharField(max_length=100)),
                ('group_name', models.CharField(max_length=100)),
                ('amount', models.BigIntegerField()),
                ('expire_days', models.FloatField(blank=True)),
                ('detail', models.CharField(max_length=100)),
                ('with_group', models.BooleanField()),
            ],
        ),
    ]
