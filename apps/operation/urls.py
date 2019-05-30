#-*- coding:utf-8 -*-
__author__ = 'wuyanli'

from django.conf.urls import url
from .views import CheckSelfScoreView,PaperListView,PaperView,SelectView,CheckStudentScoreView,AddQuestion,CheckQuestionView,AlterQuestionView,DeleteQuestion,AddQuestionTypeView



urlpatterns = [
    # 学生管理
    url(r'^paperlist/$', PaperListView.as_view(), name="paperlist"),
    # 查看学生信息
    url(r'^paper/(?P<paper_id>.*)/$', PaperView.as_view(), name="paper"),
# 删除学生
    url(r'^select/$', SelectView.as_view(), name="select"),
    url(r'^train/$', SelectView.as_view(), name="train"),
    # 在某题库添加题目
    url(r'^add_question/(?P<course_id>.*)/$', AddQuestion.as_view(), name="add_question"),
# 查看题目
    url(r'^check_question/(?P<course_id>.*)/$', CheckQuestionView.as_view(), name="check_question"),
# 修改题目
    url(r'^alter_question/(?P<question_id>.*)/$', AlterQuestionView.as_view(), name="alter_question"),
# 删除题目
    url(r'^delete_question/(?P<question_id>.*)/$', DeleteQuestion.as_view(), name="delete_question"),
# 添加题目类型
    url(r'^add_questionType/$', AddQuestionTypeView.as_view(), name="add_questionType"),
# 查看学生成绩
    url(r'^check_student_score/(?P<st_id>.*)/$', CheckStudentScoreView.as_view(), name="check_student_score"),
# 查看自己成绩
    url(r'^check_score/(?P<user_id>.*)/$', CheckSelfScoreView.as_view(), name="check_score"),



]