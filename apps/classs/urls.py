#-*- coding:utf-8 -*-
__author__ = 'wuyanli'


from django.conf.urls import url
from .views import StudentManageView,CheckAtudentInfoView,DeleteStudentView




urlpatterns = [
    # 学生管理
    url(r'^student_manage/$', StudentManageView.as_view(), name="student_manage"),
    # 查看学生信息
    url(r'^student_info/(?P<student_id>.*)/$', CheckAtudentInfoView.as_view(), name="student_info"),
# 删除学生
    url(r'^delete_student/(?P<student_id>.*)/$', DeleteStudentView.as_view(), name="delete_student"),



]