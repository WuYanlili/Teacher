# encoding=utf-8
__author__ = 'wuyanli'

import xadmin

from .models import ClassRoom,AskQuestion,StudentManagement


class ClassRoomAdmin(object):
    list_display = ['class_id', 'yard', 'class_info','grade','profession','image']
    search_fields = ['class_id', 'yard', 'class_info','grade','profession','image']
    list_filter = ['class_id', 'yard', 'class_info','grade','profession','image']


class StudentManageMentAdmin(object):
    list_display = ['classroom', 'student_id', 'student_info', 'review', 'answer']
    search_fields = ['classroom', 'student_id', 'student_info', 'review', 'answer']
    list_filter = ['classroom', 'student_id', 'student_info', 'review', 'answer']


class AskQuestionAdmin(object):
    list_display = ['ask_student', 'ask', 'question_teacher', 'qusetion']
    search_fields = ['ask_student', 'ask', 'question_teacher', 'qusetion']
    list_filter = ['ask_student', 'ask', 'question_teacher', 'qusetion']


xadmin.site.register(ClassRoom,ClassRoomAdmin)
xadmin.site.register(StudentManagement,StudentManageMentAdmin)
xadmin.site.register(AskQuestion,AskQuestionAdmin)