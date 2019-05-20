# encoding=utf-8
from django.shortcuts import render

from .models import ManageQuestion,ExplationQuestion,TextOnline


from django.http import HttpResponse
from django.views.generic.base import View
from .models import TextOnline
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from utils.mixin_utils import LoginRequiredMixin


class OnlineText(View):
    def get(self,request):
        all_text = TextOnline.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_text, 8, request=request)

        text = p.page(page)
        return render(request, "usercenter-textonline.html", {"all_text": text})


class QuestionView(View):
    def get(self,request):
        all_questions = ExplationQuestion.objects.all().order_by("-add_time")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_questions, 6, request=request)

        question = p.page(page)
        return render(request,'course-list.html',{"all_questions":question})


class QuestionDetailView(View):
    def get(self,request,question_id):
        question = ExplationQuestion.objects.get(id=int(question_id))
        video = question.url
        tag = question.tag
        if tag:
            relate_course = ExplationQuestion.objects.filter(tag=tag)[:1]
        else:
            relate_course = []
        return render(request,'course-detail.html',{
            "question":question,
            "relate_course":relate_course
        })


class QuestionVideoView(View):
    '''
    视频播放页面
    '''
    def get(self,request,question_id):
        question = ExplationQuestion.objects.get(id=int(question_id))
        return render(request,'course-video.html',{'question':question})


