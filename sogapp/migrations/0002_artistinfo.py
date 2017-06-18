# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=250)),
                ('artist_bio', models.TextField()),
                ('artist_photo', models.URLField()),
            ],
        ),
    ]
