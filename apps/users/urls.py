# encoding=utf-8
__author__ = 'wuyanli'


from django.conf.urls import url, include

from .views import UserinfoView,UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from classs.views import MyClass,ApplyClass,InterClass,AddClassView,Addclass,ModifyClass, MyQuestion
from questions.views import OnlineText
from uploadjob.views import UpLoadJobView


urlpatterns = [
    #用户信息
    url(r'^info/$', UserinfoView.as_view(),name="user_info"),
    #用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    #用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendmail"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    #我的班级
    url(r'^my_class/$', MyClass.as_view(), name="my_class"),
    #申请加入班级
    url(r'^apply_class/(?P<class_id>.*)/$', ApplyClass.as_view(), name="apply_class"),
    #加入班级
    url(r'^inter_class/(?P<class_id>.*)/$', InterClass.as_view(), name="inter_class"),
    #老师班级管理
    url(r'^manage_class/$', AddClassView.as_view(),name="manage_class"),
    #老师添加班级
    url(r'^add_class/$', Addclass.as_view(),name="add_class"),
    #修改班级
    url(r'^modify_class/(?P<class_id>.*)/$', ModifyClass.as_view(),name="modify_class"),
#     提交问题
    url(r'^submit_questions/$', MyQuestion.as_view(),name="submit_questions"),
#     在线测评
    url(r'^online_text/$', OnlineText.as_view(),name="online_text"),
#     提交作业
    url(r'^upload_job/$', UpLoadJobView.as_view(),name="upload_job"),
]