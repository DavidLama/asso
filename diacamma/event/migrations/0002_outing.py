# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date'], 'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(null=True, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.IntegerField(choices=[(0, 'examination'), (1, 'trainning/outing')], db_index=True, default=0, verbose_name='event type'),
        ),
    ]
