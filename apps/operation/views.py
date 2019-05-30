# _*_encoding:utf-8_*_
from django.shortcuts import render

from django.views.generic.base import View
from datetime import datetime
from users.models import UserProfile
from .models import UserAnswerLog, UserScore,Paper, Question, CourseList, PaperList,PaperCache
from classs.models import StudentManagement


class PaperListView(View):
    """试题列表页面"""

    def get(self, request):
        papers = PaperList.objects.filter(is_allow=True)
        courses = CourseList.objects.all()
        for i in papers:
            print i.name, '**', i.id
        return render(request, "paperlist.html", {"papers": papers, "title": u"试题列表页面",
                                                  "courses":courses})

'''添加题库'''
class AddQuestion(View):
    def get(self,request,course_id):
        course = CourseList.objects.get(id=course_id)
        return render(request,"add_question.html",{"course":course})
    def post(self,request,course_id):
        course = CourseList.objects.get(id=course_id)
        questionType = request.POST.get("questionType","")
        content = request.POST.get("content","")
        answer = request.POST.get("answer","")
        choice_a = request.POST.get("choice_a","")
        choice_b = request.POST.get("choice_b","")
        choice_c = request.POST.get("choice_c","")
        choice_d = request.POST.get("choice_d","")
        choice_e = request.POST.get("choice_e","")
        choice_f = request.POST.get("choice_f","")
        score = request.POST.get("score","")
        Question.objects.create(course=course,questionType=questionType,content=content,answer=answer,choice_a=choice_a,
                                choice_b=choice_b,choice_c=choice_c,choice_d=choice_d,choice_e=choice_e,choice_f=choice_f,
                                score=score)
        return render(request,"paperlist.html")

'''查看题目'''
class CheckQuestionView(View):
    def get(self,request,course_id):
        course = CourseList.objects.get(id=course_id)
        questions = Question.objects.filter(course=course)
        return render(request,"check_question.html",{"questions":questions})

'''修改题目'''
class AlterQuestionView(View):
    def get(self,request,question_id):
        question = Question.objects.get(id=question_id)
        return render(request,"alter_course_question.html",{"question":question})
    def post(self,request,question_id):
        questionType = request.POST.get("questionType", "")
        content = request.POST.get("content", "")
        answer = request.POST.get("answer", "")
        choice_a = request.POST.get("choice_a", "")
        choice_b = request.POST.get("choice_b", "")
        choice_c = request.POST.get("choice_c", "")
        choice_d = request.POST.get("choice_d", "")
        choice_e = request.POST.get("choice_e", "")
        choice_f = request.POST.get("choice_f", "")
        score = request.POST.get("score", "")
        Question.objects.filter(id=question_id).update(questionType=questionType,content=content,answer=answer,choice_a=choice_a,
                                                       choice_b=choice_b,choice_c=choice_c,choice_d=choice_d,choice_e=choice_e,choice_f=choice_f,
                                                       score=score)
        courses = CourseList.objects.all()
        return render(request,"paperlist.html",{"title": u"试题列表页面",
                                                  "courses":courses})


'''删除题目'''
class DeleteQuestion(View):
    def get(self,request,question_id):
        Question.objects.filter(id=question_id).delete()
        courses = CourseList.objects.all()
        return render(request, "paperlist.html", {"title": u"试题列表页面",
                                                  "courses": courses})



'''添加题库类型'''
class AddQuestionTypeView(View):
    def get(self,request):
        return render(request,"add_questionType.html")
    def post(self,request):
        course = request.POST.get("course","")
        desc = request.POST.get("desc","")
        CourseList.objects.create(name=course,decs=desc)
        courses = CourseList.objects.all()
        return render(request,"paperlist.html",{"title": u"试题列表页面",
                                                  "courses":courses})


'''查看学生成绩'''
class CheckStudentScoreView(View):
    def get(self,request,st_id):
        user = StudentManagement.objects.get(id=st_id).student_info
        course =UserScore.objects.filter(user=user)
        return render(request,"check_student_score.html",{"userscore":course})

'''查看成绩'''
class CheckSelfScoreView(View):
    def get(self,request,user_id):
        user = UserProfile.objects.get(id=user_id)
        course = UserScore.objects.filter(user=user)
        return render(request, "check_student_score.html", {"userscore": course})



class PaperView(View):
    def get(self, request, paper_id):
        if request.user.is_authenticated:
            papers = Paper.objects.filter(paper_name_id=paper_id)#找到所有试题
            question_list = []
            question_id_list = []
            # print('paper is ', papers)
            for paper in papers:
                print ('paper is ', paper)
                question = Question.objects.get(pk=paper.question_id)
                question_list.append(question)
                question_id_list.append(question.id)
            title = paper.paper_name

            print ('get 方法里用户获取的题目编号为', question_id_list)  # 显示当前题目编号列表
            question_now = tuple(question_list)  # 题目元组

            question_count = len(question_now)  # 题目数
            return render(request, "test_paper.html", {"question": question_now,
                                                           "question_count": question_count, "title": title})
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})

    def post(self, request, paper_id):
        papers = Paper.objects.filter(paper_name_id=paper_id)  # 找到所有试题
        question_id_list = []
        for paper in papers:
            print ('paper is ', paper)
            question = Question.objects.get(pk=paper.question_id)
            question_id_list.append(question.id)
        # 找到该用户所有的做题记录
        user_info = UserProfile.objects.get(username=request.user)

        title = paper.paper_name.name
        # 分数记录
        user_score = UserScore()
        # 记录用户
        user_score.user = request.user
        # 记录做题时间
        user_score.add_time = datetime.now()
        user_score.leibie = user_info.leibie
        user_score.nickname = user_info.nickname
        user_score.zhiwu = user_info.zhiwu
        user_score.danwei = user_info.danwei

        # 显示提交的题目编号列表
        temp_score = 0
        # 遍历每一道题
        user_score.paper = PaperList.objects.get(pk=paper_id)
        # 遍历每一道题
        wrong_question = []
        for i in question_id_list:
            # 根据编号找到用户提交的对应题号的答案
            user_ans = request.POST.get(str(i), "")
            print (u'试题', i, u'收到的答案是', user_ans)
            # 获取题号为 i 的题目元组对象
            temp_question = Question.objects.get(pk=i)
            # 把正确答案与提交的答案比较
            if temp_question.answer == user_ans:
                temp_score += temp_question.score
                print ("试题", temp_question.id, "答案正确")
            else:
                 question = Question.objects.get(pk=i)
                 wrong_question.append(question)
        wrong_question_now = tuple(wrong_question)
        wrong_question_count = len(wrong_question_now)
        user_score.total = temp_score
        user_score.save()
        return render(request, "score.html", {"score": user_score.total, "title": title,"wrong_question": wrong_question_now,"wrong_question_count":wrong_question_count })

def index(request):
    userinfo = UserProfile.objects.all()

    return render( request,'index.html', locals())

import random

class SelectView(View):

    def get(self, request):
        if request.user.is_authenticated:
            question_list = []
            # seq1 = [i for i in range(1, 4)]
            # seq2 = [i for i in range(4, 7)]
            # seq3 = [i for i in range(7, 10)]
            # question_id_list1 = random.sample(seq1,2 )
            # question_id_list2 = random.sample(seq2,2 )
            # question_id_list3 = random.sample(seq3,2 )
            # question_id_list1.extend(question_id_list2)
            # question_id_list1.extend(question_id_list3)
            question_id_list1 = [1,2,3,4,5]
            print question_id_list1
            for question_id in question_id_list1:
                print question_id
                question = Question.objects.get(id=question_id)
                print question
                question_list.append(question)
                Paper_Cache = PaperCache()
                Paper_Cache.question = question_id
                Paper_Cache.user = request.user
                Paper_Cache.add_time = datetime.now()
                Paper_Cache.save()
            # blogModel = BlogModel(title='我是第一篇文章标题', content='我是第一篇文章的内容')
            title = "考试"
            print 'get方法里用户获取的题目编号为', question_id_list1  # 显示当前题目编号列表
            question_now = tuple(question_list)  # 题目元组
            question_count = len(question_now)  # 题目数
            print question_now
            return render(request, "test_paper.html", {"question": question_now,"question_count": question_count, "title": title,
                                                       "question_id_list":question_id_list1})
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})

    def post(self, request):
        # # 找到该用户所有的做题记录
        question_id_list = PaperCache.objects.filter(user=request.user)
        print question_id_list.count(),"做题记录"
        user_info = UserProfile.objects.get(username=request.user)

        title = "考试"
        # 分数记录
        user_score = UserScore()
        # 记录用户
        user_score.user = request.user
        # 记录做题时间
        user_score.add_time = datetime.now()
        user_score.nickname = user_info.nick_name
        user_score.studentid = user_info.studentId
        user_score.classroom = user_info.classroom

        # 显示提交的题目编号列表
        temp_score = 0
        # 遍历每一道题
        user_score.paper = PaperList.objects.get(pk=1)
        print user_score.paper
        wrong_question = []
        for i in question_id_list:
            # 根据编号找到用户提交的对应题号的答案
            print i.id
            temp_question = Question.objects.get(pk=i.question)
            print temp_question.questionType
            if temp_question.questionType == 'mxz':
                a = str(i.question)+'_1'
                b = str(i.question)+'_2'
                c = str(i.question)+'_3'
                d = str(i.question)+'_4'
                e = str(i.question)+'_5'
                f = str(i.question)+'_6'
                user_ans1 = request.POST.get(a, "")  # 找对应题号的答案
                user_ans2 = request.POST.get(b, "")  # 找对应题号的答案
                user_ans3 = request.POST.get(c, "")  # 找对应题号的答案
                user_ans4 = request.POST.get(d, "")  # 找对应题号的答案
                user_ans5 = request.POST.get(e, "")  # 找对应题号的答案
                user_ans6 = request.POST.get(f, "")  # 找对应题号的答案
                user_ans_final = user_ans1+user_ans2+user_ans3+user_ans4+user_ans5+user_ans6
                print user_ans_final
                a = temp_question.answer
                if temp_question.answer == user_ans_final:
                    temp_score += temp_question.score
                    print("试题", temp_question.id, "答案正确")
                else:
                    question = Question.objects.get(id=i.question)
                    wrong_question.append(question)
            else:
                user_ans = request.POST.get(str(i.question), "")#找对应题号的答案
                print '试题', i, '收到的答案是', user_ans
                print user_ans,temp_question.answer
                if temp_question.answer == user_ans:
                    temp_score += temp_question.score
                    print "试题", temp_question.id, "答案正确"
                    print temp_score
                else:
                    question = Question.objects.get(id=i.question)
                    print question
                    wrong_question.append(question)
        wrong_question_now = tuple(wrong_question)
        wrong_question_count = len(wrong_question_now)
        user_score.total = temp_score
        user_score.save()
        question_id_list.delete()
        return render(request, "score.html", {"score": user_score.total, "title": title,"wrong_question": wrong_question_now,"wrong_question_count":wrong_question_count })

class TrainView(View):
    def get(self, request):
        if request.user.is_authenticated:
            question_list = []
            seq1 = [i for i in range(1, 4)]
            seq2 = [i for i in range(4, 7)]
            seq3 = [i for i in range(7, 10)]
            question_id_list1 = random.sample(seq1,2 )
            question_id_list2 = random.sample(seq2,2 )
            question_id_list3 = random.sample(seq3,2 )
            question_id_list1.extend(question_id_list2)
            question_id_list1.extend(question_id_list3)

            print(question_id_list1)
            for question_id in question_id_list1:
                question = Question.objects.get(id=question_id)
                question_list.append(question)
                Paper_Cache = PaperCache()
                Paper_Cache.question = question_id
                Paper_Cache.user = request.user
                Paper_Cache.add_time = datetime.now()
                Paper_Cache.save()
            # blogModel = BlogModel(title='我是第一篇文章标题', content='我是第一篇文章的内容')
            title = "考试"
            print ('get 方法里用户获取的题目编号为', question_id_list1)  # 显示当前题目编号列表
            question_now = tuple(question_list)  # 题目元组

            question_count = len(question_now)  # 题目数


            return render(request, "test_paper.html", {"question": question_now,"question_count": question_count, "title": title,})
        else:
            return render(request, "login.html", {"msg": u'为保证考试客观公正，考题不对未登录用户开放'})

    def post(self, request):
        # # 找到该用户所有的做题记录
        question_id_list = PaperCache.objects.filter(user=request.user)
        title = "考试"
        # 分数记录
        user_score = UserScore()
        # 记录用户
        user_score.user = request.user
        # 记录做题时间
        user_score.add_time = datetime.now()
        # 显示提交的题目编号列表
        temp_score = 0
        # 遍历每一道题
        user_score.paper = PaperList.objects.get(pk=3)
        wrong_question = []

        for i in question_id_list:
            # 根据编号找到用户提交的对应题号的答案
            temp_question = Question.objects.get(pk=i.question)

            if temp_question.questionType == 'mxz':
                a = str(i.question)+'_1'
                b = str(i.question)+'_2'
                c = str(i.question)+'_3'
                d = str(i.question)+'_4'
                e = str(i.question)+'_5'
                f = str(i.question)+'_6'
                user_ans1 = request.POST.get(a, "")  # 找对应题号的答案
                user_ans2 = request.POST.get(b, "")  # 找对应题号的答案
                user_ans3 = request.POST.get(c, "")  # 找对应题号的答案
                user_ans4 = request.POST.get(d, "")  # 找对应题号的答案
                user_ans5 = request.POST.get(e, "")  # 找对应题号的答案
                user_ans6 = request.POST.get(f, "")  # 找对应题号的答案
                user_ans_final = user_ans1+user_ans2+user_ans3+user_ans4+user_ans5+user_ans6
                print(user_ans_final)
                a = temp_question.answer
                if temp_question.answer == user_ans_final:
                    temp_score += temp_question.score
                    print("试题", temp_question.id, "答案正确")
                else:
                    question = Question.objects.get(id=i.question)
                    wrong_question.append(question)
            else:
                user_ans = request.POST.get(str(i.question), "")#找对应题号的答案
                print (u'试题', i, u'收到的答案是', user_ans)
                if temp_question.answer == user_ans:
                    temp_score += temp_question.score
                    print ("试题", temp_question.id, "答案正确")
                else:
                    question = Question.objects.get(id=i.question)
                    wrong_question.append(question)
        wrong_question_now = tuple(wrong_question)
        wrong_question_count = len(wrong_question_now)
        user_score.total = temp_score
        question_id_list.delete()
        return render(request, "score.html", {"score": user_score.total, "title": title,"wrong_question": wrong_question_now,"wrong_question_count":wrong_question_count })

