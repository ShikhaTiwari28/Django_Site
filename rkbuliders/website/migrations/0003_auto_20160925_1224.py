# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160925_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About US'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.FileField(help_text='Image should be in jpg, png or jpeg format and size be 1200px * 691px', max_length=200, upload_to='aboutus', validators=[website.models.file_extension]),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]