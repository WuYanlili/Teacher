#-*- coding:utf-8 -*-
__author__ = 'wuyanli'

from django import forms
from captcha.fields import CaptchaField


class ExamForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)