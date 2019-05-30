# encoding=utf-8
__author__ = 'wuyanli'


from django.conf.urls import url, include

from .views import UserinfoView,UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from classs.views import MyClass,ApplyClass,InterClass,Addclass,ModifyClass, MyQuestion,DeleteClass,AnswerQuestionView,UpdateAskView
from questions.views import OnlineText
from uploadjob.views import UpLoadJobView,AddReviewView, JobDescView


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
    # 删除班级
    url(r'^delete_class/(?P<class_id>.*)/$', DeleteClass.as_view(), name="delete_class"),
    #老师添加班级
    url(r'^add_class/$', Addclass.as_view(),name="add_class"),
    #修改班级
    url(r'^modify_class/(?P<class_id>.*)/$', ModifyClass.as_view(),name="modify_class"),
#     提交问题
    url(r'^submit_questions/$', MyQuestion.as_view(),name="submit_questions"),
# 学生修改问题内容
    url(r'^update_ask/(?P<ask_id>.*)/$', UpdateAskView.as_view(), name="update_ask"),
    # 教师回答,修改问题
    url(r'^answer_question/(?P<question_id>.*)/$', AnswerQuestionView.as_view(), name="answer_question"),
#     在线测评
    url(r'^online_text/$', OnlineText.as_view(),name="online_text"),
#     提交作业
    url(r'^upload_job/$', UpLoadJobView.as_view(),name="upload_job"),
# 教师点评,修改点评
    url(r'^review/(?P<job_id>.*)/$', AddReviewView.as_view(), name="review"),
# 修改作业描述
    url(r'^job_desc/(?P<job_id>.*)/$', JobDescView.as_view(), name="job_desc"),
]