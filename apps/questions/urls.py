# encoding=utf-8
__author__ = 'wuyanli'


from django.conf.urls import url, include
from .views import QuestionView, QuestionDetailView ,QuestionVideoView ,AddQuestionExplation,DeleteQuestionView,AlterQuestionView




urlpatterns = [
    #真题讲解列表列
    url(r'^list/$', QuestionView.as_view(),name="question_list"),
#     课程详情页
    url(r'^question_detail/(?P<question_id>\d+)/$', QuestionDetailView.as_view(),name="question_detail"),
#     真题视频
    url(r'^question_video/(?P<question_id>\d+)/$', QuestionVideoView.as_view(),name="question_video"),
#     添加真题
    url(r'^add_question/$', AddQuestionExplation.as_view(),name="add_question"),
#     教师删除真题
    url(r'^delete_question/(?P<question_id>\d+)/$', DeleteQuestionView.as_view(),name="delete_question"),
#     教师修改真题
    url(r'^alter_question/(?P<question_id>\d+)/$', AlterQuestionView.as_view(),name="alter_question"),




]