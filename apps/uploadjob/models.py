# _*_encoding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from datetime import datetime

# Create your models here.


class UpLoadJob(models.Model):
    job_student = models.ForeignKey(UserProfile, verbose_name=u"学生信息", on_delete=models.CASCADE,related_name='job_student')
    job = models.ImageField(upload_to="job/%Y/%m",default=u"image/default.png",max_length=100, verbose_name=u"作业内容")
    upload_time = models.DateTimeField(default=datetime.now, verbose_name=u"上传时间")
    job_desc = models.CharField(verbose_name=u"作业描述", max_length=500, null=True, blank=True)
    review_teacher = models.ForeignKey(UserProfile, verbose_name=u"点评教师", on_delete=models.CASCADE, null=True, blank=True,related_name='job_teacher')
    review = models.CharField(verbose_name=u"点评内容", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "点评作业"
        verbose_name_plural = verbose_name
