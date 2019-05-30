# _*_encoding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from users.models import UserProfile

# Create your models here.


class ManageQuestion(models.Model):
    course = models.CharField(max_length=20, verbose_name=u"课程")
    chapter = models.CharField(max_length=20, verbose_name=u"章节")
    name = models.CharField(max_length=20, verbose_name=u"章节名称")
    download = models.FileField(upload_to="classs/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"上传时间")


    class Meta:
        verbose_name=u"题型管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.course


class ExplationQuestion(models.Model):
    course = models.CharField(max_length=10, verbose_name=u"科目")
    name = models.CharField(max_length=10, verbose_name=u"年份")
    unit = models.CharField(max_length=10,verbose_name=u"第几套")
    desc = models.CharField(max_length=500,verbose_name=u"课程描述")
    video_name = models.CharField(max_length=100, verbose_name=u"视频名称")
    download = models.FileField(upload_to="question/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址",null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"上传时间")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100, default="courses/2019/05/b8.jpg")
    category = models.CharField(default=u"考研英语", max_length=20, verbose_name=u"课程类别",null=True, blank=True)
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10,null=True, blank=True)
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知",null=True, blank=True)
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你",null=True, blank=True)
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)

    class Meta:
        verbose_name=u"真题讲解"
        verbose_name_plural = verbose_name




class TextOnline(models.Model):
    text = models.CharField(verbose_name=u"题目",max_length=30)
    line = models.CharField(verbose_name=u"链接",max_length=100)
    add_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)

    class Meta:
        verbose_name = u"在线测评"
        verbose_name_plural = verbose_name

