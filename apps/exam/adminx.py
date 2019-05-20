#-*- coding:utf-8 -*-
__author__ = 'wuyanli'


import xadmin

from .models import StudentExam,ImportQuestion


class ImportQuestionAdmin(object):
    list_display = ['questionID', 'teacher', 'title','standardAnswer']
    search_fields = ['questionID', 'teacher', 'title','standardAnswer']
    list_filter = ['questionID', 'teacher', 'title','standardAnswer']


class StudentExamAdmin(object):
    list_display = ['student', 'score']
    search_fields = ['student', 'score']
    list_filter = ['student', 'score']




xadmin.site.register(StudentExam,StudentExamAdmin)
xadmin.site.register(ImportQuestion,ImportQuestionAdmin)