# _*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from .models import UpLoadJob
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UpLoadJobForm
from django.http import HttpResponse
import os


class UpLoadJobView(View):
    def get(self,request):
        all_job = UpLoadJob.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_job, 1, request=request)

        job = p.page(page)
        return render(request, "usercenter-submitjob.html", {"all_job": job})
    def post(self,request):
        upload_form = UpLoadJobForm(request.POST)
        job_img = request.FILES.get('file')
        job_desc = request.POST.get('job_desc', '')
        # if upload_form.is_valid():
        # job_img = request.file.get('file')
        # job_desc = request.POST.get('job_desc','')
        job = UpLoadJob()
        job.job_student = self.request.user
        job.job = job_img
        job.job_desc = job_desc
        job.save()
        return render(request,'usercenter-submitjob.html')
        # else:
        #     return render(request,"404.html")