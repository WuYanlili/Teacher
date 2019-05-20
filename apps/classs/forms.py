# encoding=utf-8
__author__ = 'wuyanli'

from .models import ClassRoom,StudentManagement
from django import forms


class AddClassForm(forms.Form):
    class_id = forms.CharField(required=True,max_length=15)
    yard = forms.CharField(required=True,max_length=10)
    profession = forms.CharField(required=True,max_length=10)
    grade = forms.CharField(required=True,max_length=10)
    class_info = forms.CharField(required=True,max_length=500)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['image']


class AskQuestionForm(forms.Form):
    ask = forms.CharField(required=True,max_length=500)
    ask_student = forms.CharField(required=True)