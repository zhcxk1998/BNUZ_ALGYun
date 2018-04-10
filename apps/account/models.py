from django.db import models

# Create your models here.
# 用户信息
class User(models.Model):
    # === 基本信息 ===
    id = models.CharField(max_length=50, primary_key=True)  # 用户ID（学号、工号、账号）

    password = models.CharField(max_length=100, blank=True, null=True)  # 用户密码

    sex = models.SmallIntegerField(blank=False, null=False, default=-1)  # 用户性别

    realname = models.CharField(max_length=50, blank=True, null=True)  # 真实姓名

    nickname = models.CharField(max_length=50, blank=True, null=True)  # 用户昵称

    headimg = models.CharField(max_length=50, blank=True, null=True)  # 用户头像

    email = models.EmailField(blank=True, null=True)  # 用户邮箱

    # === 安全设置 ===

    email_validated = models.BooleanField(blank=False, null=False, default=False)           # 邮箱是否认证

    email_findpwd_validated = models.CharField(max_length=100, blank=True, null=True)       # 邮箱验证用的token

    def __str__(self):
        return u'id = %s，昵称：%s，真实姓名：%s，Email:%s' % (self.id, self.nickname, self.realname, self.email)