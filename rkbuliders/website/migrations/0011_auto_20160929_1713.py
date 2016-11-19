# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20160928_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.FileField(help_text='Image should be in jpg, png or jpeg format and should be small image.', max_length=200, upload_to='reviews', validators=[website.models.file_extension]),
        ),
    ]