from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from shortid import short_id
import json
from django.forms.models import model_to_dict
from .models import Users
from django.http import Http404
import requests
import markdown
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
        user_correct = Users.objects.filter(username=username, password=password)
        if user_correct:
            request.session['is_login'] = True
            user_one =Users.objects.get(username=username)
            user_one_dict = model_to_dict(user_one)
            request.session['nickname'] = user_one_dict['nickname']
            # 设置session持续时间
            request.session.set_expiry(60*30)

            return HttpResponseRedirect('/index')

        elif not Users.objects.filter(username=username):
            notice = '不存在该用户'
            return render(request,'article/login.html',{'notice':notice})

        elif not Users.objects.filter(password=password):
            notice = '密码错误'
            return render(request,'article/login.html',{'notice':notice})

def logout(request):

    if request.session.get('is_login', None):
        request.session['is_login'] = False
        return render(request,'article/logout.html')
    else:
        return HttpResponseRedirect('/login')

# # 文章详情
# def detail(request,id):
#     query_set = {}
#     # 如果是数字就是id，不是就是sid
#     if id.isdigit():
#         query_set["id"] = id
#     else:
#         query_set["sid"] = id
#
#     # 查询一条数据
#     article = None
#     try:
#         article = Article.objects.get(**query_set)
#
#     except Article.DoesNotExist:
#         raise Http404
#
#     # 修改点击量
#     article.hits += 1
#     article.save()
#
#     # 如果是markdown，就用markdown渲染
#
#     article.content = markdown.markdown(article.content, extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         'markdown.extensions.toc',
#     ], safe_mode=True, enable_attributes=False)
#
#     sid = short_id.get_short_id()
#     request.session['sid'] = sid
#
#     return render(request, "article/detail.html", {
#         'id': id,
#         'article': article,
#         'sid': sid
#     })
