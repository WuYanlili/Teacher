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
        all_class = ClassRoom.objects.all().order_by("class_id")
        status = request.user.status
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_class, 3, request=request)
        class1 = p.page(page)
        if status=="teacher":
            return render(request, "usercenter-my-class.html", {"all_class": class1})
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

'''
修改班级
'''
class ModifyClass(View):
    def get(self, request,class_id):
        classs = ClassRoom.objects.get(id=int(class_id))
        return render(request, 'modify-class.html', {"classs": classs})
    def post(self,request,class_id):
        classs = ClassRoom.objects.get(id=int(class_id))
        print classs
        classs.class_id = request.POST.get("class_id","")
        classs.grade = request.POST.get("grade","")
        classs.yard = request.POST.get("yard","")
        classs.profession = request.POST.get("profession","")
        classs.class_info = request.POST.get("class_info","")
        print request.POST.get("class_info","")
        classs.save()
        all_class = ClassRoom.objects.all().order_by("class_id")
        return render(request, "usercenter-my-class.html", {"all_class":all_class})

'''
教师删除班级
'''
class DeleteClass(View):
    def get(self,request,class_id):
        ClassRoom.objects.filter(class_id=class_id).delete()
        all_class = ClassRoom.objects.all().order_by("class_id")
        return render(request,"usercenter-my-class.html",{"all_class":all_class})
    def post(self,request):
        all_class = ClassRoom.objects.all().order_by("class_id")
        return render(request,"usercenter-my-class.html",{"all_class":all_class})



'''
学生进入班级
'''
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




'''
    添加班级
'''
class Addclass(View):

    def get(self,request):
        return render(request,"add_class.html")
    def post(self, request):
        class_id = request.POST.get("class_id","")
        yard = request.POST.get("yard","")
        profession = request.POST.get("profession","")
        grade = request.POST.get("grade","")
        class_info = request.POST.get("class_info","")
        ClassRoom.objects.create(class_id=class_id,yard=yard,profession=profession,grade=grade,class_info=class_info)
        all_class = ClassRoom.objects.all().order_by("class_id")
        return render(request,"usercenter-my-class.html",{"all_class":all_class})

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
        ask = request.POST.get("ask", "")
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        ask = request.POST.get("ask", "")
        ask_student = self.request.user
        askquestion = AskQuestion()
        askquestion.ask = ask
        askquestion.ask_student = ask_student
        askquestion.save()
        all_comments = AskQuestion.objects.all().order_by("-id")
        return render(request, "usercenter-myquestion.html",{
            "all_comments": all_comments
        })


'''
教师回答修改问题
'''
class AnswerQuestionView(View):
    def get(self,request):
        return render(request,"usercenter-my-class.html")

    def post(self,request,question_id):
        answer = request.POST.get("answer","")
        question = AskQuestion.objects.get(id=question_id)
        question.question_teacher = request.user
        question.qusetion = answer
        question.save()
        all_comments = AskQuestion.objects.all().order_by("-id")
        return render(request,"usercenter-myquestion.html",{"all_comments":all_comments})


'''
学生修改问题内容
'''
class UpdateAskView(View):
    def post(self,request,ask_id):
        ask = request.POST.get("ask","")
        AskQuestion.objects.filter(id=ask_id).update(ask=ask)
        all_comments = AskQuestion.objects.all().order_by("-id")
        return render(request, "usercenter-myquestion.html", {"all_comments": all_comments})


'''
学生管理
'''
class StudentManageView(View):
    def get(self,request):
        students = UserProfile.objects.filter(status='student')
        sts = StudentManagement.objects.all().order_by("student_id")
        return render(request,"student_management.html",{"students":students,
                                                        "sts":sts })


'''
查看学生信息
'''
class CheckAtudentInfoView(View):
    def get(self,request,student_id):
        stmanage = StudentManagement.objects.get(id = student_id)
        student = stmanage.student_info
        print student
        return render(request,"student_info.html",{"student":student})
    def post(self,request,student_id):
        classroom = request.POST.get("classroom","")
        st_id = request.POST.get("student_id","")
        mobile = request.POST.get("mobile","")
        # address = request.POST.get("address","")
        gender = request.POST.get("gender","")
        # birday = request.POST.get("birday","")
        # nick_name = request.POST.get("nick_name","")
        user = UserProfile.objects.get(id=int(student_id))
        student = StudentManagement.objects.get(student_info=user)
        print user,classroom,st_id,mobile,student_id
        print user.is_authenticated()
        user.classroom = classroom
        user.studentId = st_id
        user.mobile = mobile
        # user.address = address
        user.gender = gender
        # user.birday = birday
        # user.nick_name = nick_name
        user.save()
        student.student_id = st_id
        student.save()
        sts = StudentManagement.objects.all().order_by("student_id")
        return render(request,"student_management.html",{"sts":sts })


'''
删除学生
'''
class DeleteStudentView(View):
    def get(self,request,student_id):
        StudentManagement.objects.filter(id=student_id).delete()
        sts = StudentManagement.objects.all().order_by("student_id")
        return render(request, "student_management.html", {"sts": sts})