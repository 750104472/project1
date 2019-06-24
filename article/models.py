from django.db import models

# Create your models here.

class User(models.Model):
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