# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('updated', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('location', models.CharField(max_length=1000)),
                ('leader_name', models.CharField(max_length=100)),
                ('leader_email', models.EmailField(max_length=100, blank=True)),
                ('leader_phone', models.CharField(max_length=100, blank=True)),
                ('leader_lineid', models.CharField(max_length=100, blank=True)),
                ('activity_fee', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createby', models.CharField(max_length=100, blank=True, default='system')),
                ('updateby', models.CharField(max_length=100, blank=True, default='system')),
            ],
        ),
    ]
