from django.db import models

# Create your models here.

# 用户认证基本信息
class User(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=20)
    password = models.CharField(verbose_name='密码', max_length=12)
    email = models.EmailField(verbose_name='邮箱')

    class Meta:
        verbose_name_plural = '用户'
        db_table = 'user'