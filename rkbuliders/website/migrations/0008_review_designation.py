# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='designation',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
