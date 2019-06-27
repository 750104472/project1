from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
# Create your models here.

class Users(models.Model):
    nickname = models.CharField(max_length=20,verbose_name='昵称',blank=False,null=False)
    username = models.CharField(max_length=20,verbose_name='用户名',blank=False,null=False)
    password = models.CharField(max_length=20, verbose_name='密码', blank=False, null=False)
    createDate = models.DateTimeField(verbose_name='创建日期',auto_now_add=True)
    updateDate = models.DateTimeField(verbose_name='更新日期',auto_now=True)
    type_choice = ((1, '普通用户'),(2, '管理员'))
    type = models.IntegerField(choices=type_choice,verbose_name='用户类型',db_index=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='分类名', blank=False, null=False)
    date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    display = models.BooleanField(verbose_name='显示', default=True, db_index=True)
    sort = models.IntegerField(verbose_name='排序', default=0, db_index=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类管理"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='脚本名称', blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='脚本分类',
                                 db_index=True)

    markdown = models.BooleanField(verbose_name='markdown格式', default=True, editable=False)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='发布者', null=True, editable=False)
    hits = models.IntegerField(verbose_name='点击量', default=0, editable=False)
    content = MDTextField(verbose_name='脚本内容')
    createDate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    updateDate = models.DateTimeField(verbose_name='更新日期',auto_now=True)
    top_choices = ((0, '否'),
                   (1, '是'),)
    top = models.IntegerField(choices=top_choices, verbose_name='置顶', default=0, db_index=True)



    class Meta:
        verbose_name = "脚本"
        verbose_name_plural = "脚本管理"