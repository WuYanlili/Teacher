# _*_encoding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from datetime import datetime

# Create your models here.


class ImportQuestion(models.Model):
    teacher = models.ForeignKey(UserProfile,verbose_name=u'录入教师',max_length=50)
    questionID = models.CharField(verbose_name=u'题目类型',max_length=20)
    title = models.CharField(verbose_name=u'题目',max_length=500)
    standardAnswer = models.CharField(verbose_name=u'标准答案',max_length=50,null=True)

    class Meta:
        verbose_name = "录入题库"
        verbose_name_plural = verbose_name


class StudentExam(models.Model):
    # question = models.ForeignKey(ImportQuestion,verbose_name=u'题目')
    student = models.ForeignKey(UserProfile,verbose_name=u"测试学生",max_length=50)
    # testTime = models.DateTimeField(verbose_name=u'答题时间',auto_now=True)
    # stuAnswer = models.CharField(verbose_name=u'学生答案',max_length=50)
    # ture_or_false = models.IntegerField(verbose_name=u'是否答对',null=True)
    score = models.CharField(verbose_name=u"学生成绩", max_length=5)
    class Meta:
        verbose_name = "学生成绩"
        verbose_name_plural = verbose_name




