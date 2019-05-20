# encoding=utf-8
__author__ = 'wuyanli'


import xadmin

from .models import UpLoadJob


class UpLoadJobAdmin(object):
    list_display = ['job_student','job','upload_time','review_teacher','review']
    search_fields = ['job_student','job','upload_time','review_teacher','review']
    list_filter = ['job_student','job','upload_time','review_teacher','review']


xadmin.site.register(UpLoadJob,UpLoadJobAdmin)