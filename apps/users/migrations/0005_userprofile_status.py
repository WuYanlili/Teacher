# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-04-18 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190410_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('teacher', '\u8001\u5e08'), ('student', '\u5b66\u751f')], default='student', max_length=10),
        ),
    ]
