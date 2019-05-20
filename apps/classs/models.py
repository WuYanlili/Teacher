# _*_encoding:utf-8_*_

from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from datetime import datetime


class ClassRoom(models.Model):
    class_id = models.CharField(verbose_name=u"班级号", max_length=15)
    yard = models.CharField(verbose_name=u"所属院", max_length=10)
    class_info = models.CharField(verbose_name=u"班级公告", null=True, blank=True, max_length=500)
    grade = models.CharField(verbose_name=u"年级", max_length=10)
    profession = models.CharField(verbose_name=u"专业", max_length=10)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.class_id


class StudentManagement(models.Model):
    classroom = models.ForeignKey(ClassRoom, verbose_name=u"班级", on_delete=models.CASCADE ,null=True,blank=True)
    student_id = models.CharField(verbose_name=u"学号", max_length=15)
    student_info = models.ForeignKey(UserProfile, verbose_name=u"学生信息", on_delete=models.CASCADE)
    review = models.ImageField(upload_to="classs/resource/%Y/%m", verbose_name=u"作业检查", max_length=300, null=True,
                              blank=True)
    answer = models.CharField(max_length=100, verbose_name=u"作业点评", null=True, blank=True)

    class Meta:
        verbose_name = "学生管理"
        verbose_name_plural = verbose_name


class AskQuestion(models.Model):
    ask_student = models.ForeignKey(UserProfile, verbose_name=u"提问学生", on_delete=models.CASCADE,related_name='student')
    ask = models.CharField(verbose_name=u"学生问题", max_length=500, null=True, blank=True)
    question_teacher = models.ForeignKey(UserProfile, verbose_name=u"回答教师", on_delete=models.CASCADE, null=True, blank=True,related_name='teacher')
    qusetion = models.CharField(verbose_name=u"教师回答", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "问题答疑"
        verbose_name_plural = verbose_name
