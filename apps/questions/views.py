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

        p = Paginator(all_text, 5, request=request)

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
        all_question = ExplationQuestion.objects.all().order_by("-id")[:2]
        return render(request,'course-list.html',{"all_questions":question,
                                                  "all_question":all_question})


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


'''
教师新建真题讲解
'''
class AddQuestionExplation(View):
    def get(self,request):
        return render(request,'add_question_explation.html')
    def post(self,request):
        course = request.POST.get("course","")
        name = request.POST.get("name","")
        unit = request.POST.get("unit","")
        desc = request.POST.get("desc","")
        video_name = request.POST.get("video_name","")
        download = request.POST.get("download","")
        url = request.POST.get("url","")
        category = request.POST.get("category","")
        tag = request.POST.get("tag","")
        youneed_know = request.POST.get("youneed_know","")
        teacher_tell = request.POST.get("teacher_tell","")
        degree = request.POST.get("degree","")
        ExplationQuestion.objects.create(course=course,name=name,unit=unit,desc=desc,video_name=video_name,
                                         download=download,url=url,category=category,tag=tag,youneed_know=youneed_know,
                                         teacher_tell=teacher_tell,degree=degree)
        all_questions = ExplationQuestion.objects.all().order_by("-add_time")
        return render(request,"course-list.html",{"all_questions":all_questions})


'''
教师删除真题讲解
'''
class DeleteQuestionView(View):
    def get(self,request,question_id):
        ExplationQuestion.objects.filter(id=question_id).delete()
        all_questions = ExplationQuestion.objects.all().order_by("-add_time")
        all_question = ExplationQuestion.objects.all().order_by("-id")[:2]
        return render(request, 'course-list.html', {"all_questions": all_questions,
                                                    "all_question": all_question})

'''
教师修改真题
'''
class AlterQuestionView(View):
    def get(self,request,question_id):
        question = ExplationQuestion.objects.get(id=question_id)
        return render(request,"alter_question.html",{"question":question})
    def post(self,request,question_id):
        course = request.POST.get("course","")
        name = request.POST.get("name","")
        unit = request.POST.get("unit","")
        desc = request.POST.get("desc","")
        video_name = request.POST.get("video_name","")
        url = request.POST.get("url","")
        category = request.POST.get("category","")
        tag = request.POST.get("tag","")
        youneed_know = request.POST.get("youneed_know","")
        teacher_tell = request.POST.get("teacher_tell","")
        degree = request.POST.get("degree","")
        ExplationQuestion.objects.filter(id=question_id).update(course=course,name=name,unit=unit,desc=desc,
                                                                           video_name=video_name,url=url,category=category,
                                                                           tag=tag,youneed_know = youneed_know,teacher_tell=teacher_tell,
                                                                           degree=degree)
        all_questions = ExplationQuestion.objects.all().order_by("-add_time")
        all_question = ExplationQuestion.objects.all().order_by("-id")[:2]
        return render(request, 'course-list.html', {"all_questions": all_questions,
                                                    "all_question": all_question})