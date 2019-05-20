# encoding=utf-8
__author__ = 'wuyanli'


from django.conf.urls import url, include
from .views import QuestionView, QuestionDetailView ,QuestionVideoView




urlpatterns = [
    #真题讲解列表列
    url(r'^list/$', QuestionView.as_view(),name="question_list"),
#     课程详情页
    url(r'^question_detail/(?P<question_id>\d+)/$', QuestionDetailView.as_view(),name="question_detail"),
#     真题视频
    url(r'^question_video/(?P<question_id>\d+)/$', QuestionVideoView.as_view(),name="question_video"),



]