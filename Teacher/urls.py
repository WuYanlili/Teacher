"""Teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from Teacher.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ActiveUserView, ForgetView, ResetView, ModifyPwdView ,LogoutView

urlpatterns = [
    url(r'^teacher/', xadmin.site.urls,name='teacher'),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'activity/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget', ForgetView.as_view(), name="forget_pwd"),
    url(r'^modify_pwd', ModifyPwdView.as_view(), name="modify_psw"),
    url(r'reset/(?P<active_code>.*)/$', ResetView.as_view(), name="user_active"),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    url(r'^users/', include('users.urls',namespace="users")),
    url(r'^questions/', include('questions.urls',namespace="questions")),
    url(r'^exam/', include('exam.urls',namespace="exam")),
    url(r'^class/', include('classs.urls',namespace="class")),
    url(r'^operation/', include('operation.urls',namespace="operation")),

]