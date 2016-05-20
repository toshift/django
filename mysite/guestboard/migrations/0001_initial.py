# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe3\x81\x82\xe3\x81\xaa\xe3\x81\x9f\xe3\x81\xae\xe5\x90\x8d\xe5\x89\x8d\xe3\x82\x92\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84', max_length=64, verbose_name=b'\xe5\x90\x8d\xe5\x89\x8d')),
                ('message', models.CharField(help_text=b'\xe3\x83\xa1\xe3\x83\x83\xe3\x82\xbb\xe3\x83\xbc\xe3\x82\xb8\xe3\x82\x92\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84', max_length=255, verbose_name=b'\xe3\x83\xa1\xe3\x83\x83\xe3\x82\xbb\xe3\x83\xbc\xe3\x82\xb8')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x99\xbb\xe9\x8c\xb2\xe6\x97\xa5\xe6\x99\x82')),
            ],
        ),
    ]
