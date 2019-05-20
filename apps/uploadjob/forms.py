# encoding=utf-8
__author__ = 'wuyanli'
from django import forms

from .models import UpLoadJob


class UpLoadForm(forms.ModelForm):
    class Meta:
        model = UpLoadJob
        fields = ['job_student','job','upload_time', 'job_desc', 'review_teacher', 'review']


class UpLoadJobForm(forms.Form):
    job = forms.ImageField(required=True)
    job_desc = forms.CharField(required=True)