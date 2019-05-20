# encoding=utf-8
from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from .models import ClassRoom, StudentManagement, AskQuestion
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from forms import AddClassForm,AskQuestionForm
from django.http import HttpResponse
from utils.mixin_utils import LoginRequiredMixin
from users.models import UserProfile


class MyClass(View):
    def get(self,request):
        all_class = ClassRoom.objects.all()
        status = request.user.status
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_class, 4, request=request)
        class1 = p.page(page)
        if status=="teacher":
            return render(request, "teacher_class_detail.html", {"all_class": class1})
        else:
            id = request.user.classroom
            if request.user.classroom=='0':
                return render(request, "usercenter-my-class.html", {"all_class": class1})
            else:
                class1 = ClassRoom.objects.get(class_id=id)
                student = StudentManagement()
                student.classroom = class1
                student.student_info = request.user
                student.save()
                student_id = '1507094206'
                return render(request,"usercenter-my-class.html",{'classs':class1,'stuId':student_id})



class ApplyClass(View):
    def get(self, request,class_id):
        status = request.user.status
        if status=="teacher":
            classs = ClassRoom.objects.get(id=int(class_id))
            return render(request, 'modify-class.html', {"classs": classs})
        else:
            classs = ClassRoom.objects.get(id=int(class_id))
            return render(request, 'class-detail.html', {"classs":classs})


class ModifyClass(View):
    def get(self, request,class_id):
        classs = ClassRoom.objects.get(id=int(class_id))
        return render(request, 'modify-class.html', {"classs": classs})
    def post(self,request):
        addclass_from = AddClassForm(request.POST)
        if addclass_from.is_valid():
            class_id1 = request.POST.get("class_id", "")
            yard1 = request.POST.get("yard", "")
            class_info1 = request.POST.get("class_info", "")
            grade1 = request.POST.get("grade", "")
            profession1 = request.POST.get("profession", "")
            # img = Img(img_url=request.FILES.get('img'))
            class_room = ClassRoom()
            class_room.class_id = class_id1
            class_room.yard = yard1
            class_room.class_info = class_info1
            class_room.grade = grade1
            class_room.profession = profession1
            # class_room.image = image_form
            class_room.save()
            return render(request, "teacher_class_detail.html")
        else:
            return render(request, "teacher_class_detail.html", {"addclass_form": addclass_from})


class InterClass(View):
    def get(self,request,class_id):
        classs = ClassRoom.objects.get(id=int(class_id))
        student = request.user
        id = classs.class_id
        StudentManagement.objects.filter(student_info=student).update(classroom=classs)
        UserProfile.objects.filter(username=student).update(classroom=id)
        return render(request, 'class-detail.html', {"classs":classs})

    def post(self,request,class_id):
        classs = ClassRoom.objects.get(id=int(class_id))
        return render(request, 'class-detail.html', {"classs":classs})


class AddClassView(View):
    '''进入添加班级界面'''
    def get(self, request):
        addclass_from= AddClassForm()

        return render(request, "add_class.html", {})

'''
    添加班级
'''
class Addclass(View):

    def post(self, request):
        addclass_from= AddClassForm(request.POST)
        yard1 = request.POST.get("yard", "")
        class_id1 = request.POST.get("class_id", "")
        class_info1 = request.POST.get("class_info", "")
        grade1 = request.POST.get("grade", "")
        profession1 = request.POST.get("profession", "")
        if addclass_from.is_valid():
            class_id1 = request.POST.get("class_id","")
            if ClassRoom.objects.filter(class_id=class_id1):
                return render(request, "add_class.html", {"addclass_from": addclass_from, "msg": "该班级已经存在"})
            yard1 = request.POST.get("yard", "")
            class_info1 = request.POST.get("class_info","")
            grade1 = request.POST.get("grade","")
            profession1 = request.POST.get("profession","")
            # img = Img(img_url=request.FILES.get('img'))
            class_room = ClassRoom()
            class_room.class_id = class_id1
            class_room.yard = yard1
            class_room.class_info = class_info1
            class_room.grade = grade1
            class_room.profession = profession1
            # class_room.image = image_form
            class_room.save()
            return render(request, "teacher_class_detail.html")
        else:
            return render(request, "teacher_class_detail.html",{"addclass_form": addclass_from})

'''
提出问题
'''
class MyQuestion(LoginRequiredMixin, View):
    def get(self, request):
        all_comments = AskQuestion.objects.all().order_by("-id")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_comments, 2, request=request)

        comments = p.page(page)
        return render(request, "usercenter-myquestion.html", {
            "all_comments": comments
        })


    def post(self, request):
        askquestionfrom = AskQuestionForm(request.POST)
        ask = request.POST.get("ask", "")
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        askquestionfrom = AskQuestionForm(request.POST)
        ask = request.POST.get("ask", "")
        ask_student = self.request.user
        askquestion = AskQuestion()
        askquestion.ask = ask
        askquestion.ask_student = ask_student
        askquestion.save()
        # return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        return render(request, "usercenter-myquestion.html")







