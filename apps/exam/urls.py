#-*- coding:utf-8 -*-
__author__ = 'wuyanli'


from django.conf.urls import url, include
from .views import StudentExamView




urlpatterns = [
    #真题讲解列表列
    url(r'^student_exam/$', StudentExamView.as_view(),name="student_exam"),



]