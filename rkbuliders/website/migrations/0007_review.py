# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20160926_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(help_text='Image should be in jpg, png or jpeg format and should be small image.', max_length=200, upload_to='ourwork', validators=[website.models.file_extension])),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
