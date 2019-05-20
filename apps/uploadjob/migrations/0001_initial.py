# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-05-10 11:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UpLoadJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ImageField(default='image/default.png', upload_to='job/%Y/%m', verbose_name='\u4f5c\u4e1a\u5185\u5bb9')),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u4e0a\u4f20\u65f6\u95f4')),
                ('job_desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='\u4f5c\u4e1a\u63cf\u8ff0')),
                ('review', models.CharField(blank=True, max_length=500, null=True, verbose_name='\u70b9\u8bc4\u5185\u5bb9')),
                ('job_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_student', to=settings.AUTH_USER_MODEL, verbose_name='\u5b66\u751f\u4fe1\u606f')),
                ('review_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_teacher', to=settings.AUTH_USER_MODEL, verbose_name='\u70b9\u8bc4\u6559\u5e08')),
            ],
            options={
                'verbose_name': '\u4e0a\u4f20\u4f5c\u4e1a',
                'verbose_name_plural': '\u4e0a\u4f20\u4f5c\u4e1a',
            },
        ),
    ]
