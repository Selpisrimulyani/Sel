# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('konten', models.TextField()),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
    ]