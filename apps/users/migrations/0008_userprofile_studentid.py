# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-05-24 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='studentId',
            field=models.CharField(default='0', max_length=10, verbose_name='\u5b66\u53f7'),
        ),
    ]
