from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from .models import User
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密码', max_length=12)
    email = forms.EmailField(label='邮箱')



# 用户注册
def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid(): # 如果提交的表单合法
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            # 创建用户并保存
            obj = User.objects.create(username=username, password=password, email=email)
            obj.save()

            return HttpResponse('<h1>register success</h1>')
    else:
        userform = UserForm()
    return render(request, 'register.html', {'userform':userform})
    # return HttpResponse('test')
# 用户登录
def login(requests):
    if requests.method == 'POST':
        userform = UserForm(requests.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            # 用户验证
            user = User.objects.filter(username__exact=username, password__exact=password)

            if user:
                return render(requests, 'login_success.html')
            else:
                return HttpResponse('用户名或密码错误')
    else:
        userform = UserForm()
    return render(requests, 'login.html', {'userform':userform})