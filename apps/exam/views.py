# _*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from random import choice
from django.db.models import F

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import StudentExam,ImportQuestion

# Create your views here.


class StudentExamView(View):
    def get(self,request):
        all_questions = ImportQuestion.objects.all()
        count = all_questions.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_questions, 6, request=request)
        all_question = p.page(page)
        return render(request,'textonline.html',{'all_question':all_question,'count':count})

    def post(self,request):
        score = StudentExam()
        lists = request.POST.get('lists','')
        print lists
        false = lists.count('1')
        print request.user
        score.student = request.user
        score.score = false*20
        sc = false*10
        score.save()
        return render(request,'score.html',{'sc':sc})

# class StudentExamView(View):
#     def get(self,request):
#         currentQuestion = request.GET.get('id','')
#         studentAnswer = request.GET.get('stuAnswer','')
#         if currentQuestion and studentAnswer and ImportQuestion.objects.filter(id=currentQuestion).count()==0:
#             StudentExam(student=request.user,
#                         stuAnswer=studentAnswer).save()
#         ids = StudentExam.objects.filter(student=request.user).values_list('id')
#         ids = [item[0] for item in ids]
#         if len(ids) == 5:
#             score =
