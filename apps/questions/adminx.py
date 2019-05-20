# encoding=utf-8
__author__ = 'wuyanli'


import xadmin

from .models import ManageQuestion,ExplationQuestion,TextOnline


class ManageQuestionAdmin(object):
    list_display = ['course','chapter','name','download','add_time']
    search_fields = ['course','chapter','name','download','add_time']
    list_filter = ['course','chapter','name','download','add_time']


class ExplationQuestionAdmin(object):
    list_display = ['course', 'name', 'unit', 'download', 'add_time','url']
    search_fields = ['course','name', 'unit', 'download', 'add_time','url']
    list_filter = ['course', 'name', 'unit', 'download', 'add_time','url']


class TextOnlineAdmin(object):
    list_display = ['text', 'line', 'add_time']
    search_fields = ['text', 'line', 'add_time']
    list_filter = ['text', 'line', 'add_time']


xadmin.site.register(ManageQuestion,ManageQuestionAdmin)
xadmin.site.register(ExplationQuestion,ExplationQuestionAdmin)
xadmin.site.register(TextOnline,TextOnlineAdmin)
