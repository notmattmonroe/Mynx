# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-13 00:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('showmanager', '0002_auto_20171228_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
    ]