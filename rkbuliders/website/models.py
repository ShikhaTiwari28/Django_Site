from __future__ import unicode_literals
import os
from django.db import models

from django.core.exceptions import ValidationError


def file_extension(file_object):
    ext_list = ['.jpg', '.png', '.jpeg']
    ext = os.path.splitext(file_object.path)[-1]
    if ext.lower() not in ext_list:
        raise ValidationError('Invalid image format.')


# Create your models here.
class SliderImage(models.Model):
    """
        Model for Main Slider
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='slideshow',
                             max_length=200,
                             validators=[file_extension],
                             help_text='Image should be in jpg, png or jpeg format and size be 2000px * 1000px')
    datetime = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    """
        Model for about us info
    """
    description = models.TextField()
    sidebar_description = models.TextField()
    image = models.FileField(upload_to='aboutus',
                             max_length=200,
                             validators=[file_extension],
                             help_text='Image should be in jpg, png or jpeg format and size be 1200px * 691px')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'About US'


class ContactInfo(models.Model):
    """
        Model for contact info and address
    """
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name_plural = 'Contact Info'

class Project(models.Model):
    """
        Model for project (What we do.)
    """
    project_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='ourwork',
                             max_length=200,
                             validators=[file_extension],
                             help_text='Image should be in jpg, png or jpeg format.')
    datetime = models.DateTimeField(auto_now_add=True)

class WhatIsVastu(models.Model):
    """
        Model for what is vastu answer
    """
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'WhatIsVastu'


class Review(models.Model):
    """
        Model for testimonial
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=100)
    image = models.FileField(upload_to='reviews',
                             max_length=200,
                             validators=[file_extension],
                             help_text='Image should be in jpg, png or jpeg format and should be small image.')
    datetime = models.DateTimeField(auto_now_add=True)


class Query(models.Model):
    """
        Messages queries from talk to us form
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Queries'
