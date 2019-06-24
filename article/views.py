from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from shortid import short_id
import json
from django.forms.models import model_to_dict
from .models import User
import requests

# Create your views here.
def index(request):
    return render(request,'article/index.html')

def login(request):
    if request.method == 'GET':
        if request.session.get('is_login', None):
            return redirect('/index')
            # return redirect('/index')
        return render(request,'article/login.html')

    else:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        request.session['username']=username
        request.session['password'] = password

        if User.objects.filter(username=username, password=password):
            request.session['is_login'] = True
            return HttpResponseRedirect('/index')

        elif not User.objects.filter(username=username):
            notice = '不存在该用户'
            return render(request,'article/login.html',{'notice':notice})

        elif not User.objects.filter(password=password):
            notice = '密码错误'
            return render(request,'article/login.html',{'notice':notice})

def logout(request):

    if request.session.get('is_login', None):
        request.session['is_login'] = False
        return render(request,'article/logout.html')
    else:
        return HttpResponseRedirect('/login')
