from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import User
# Create your views here.

def login(request):
    """
    登录
    """
    if request.method == 'POST':
        res = {}
        if 'sub' in request.POST: #处理表单中的登录
            username = request.POST['name']
            userpwd = request.POST['password']
            tmp = User.objects.filter(name = username).exists()
            print(tmp)
             
            if tmp: #若表中存在该用户名数据，则已注册
                is_reg = User.objects.filter(name = username, password = userpwd).exists()
                if is_reg: #若查询有结果
                    return redirect('/accounts/index')
                else: #若查询无结果，则用户名或密码错误
                    res['rlt'] = '用户名或密码错误'
                    return render(request, 'accounts/login.html', res)
            else:#若表中无该用户名数据，则未注册
                res['rlt'] = '该用户名未注册，请注册后登录'
                return render(request, 'accounts/login.html', res)
        elif 'reg1' in request.POST: #处理表单中的注册，界面跳转
            return redirect('/accounts/register')
        else:
            pass
    return render(request,'accounts/login.html')

def register(request):
    """
    注册
    """
    if request.method == 'POST':
        res = {}
        if 'reg2' in request.POST: #处理表单中的注册
            username = request.POST['name']
            userpwd = request.POST['password']
            tmp = User.objects.filter(name = username).exists()
            if tmp: #若存在该用户名相关数据，则用户已注册
                res['rlt'] = '该用户名已注册'
                return render(request, 'accounts/register.html', res)
            else: #用户未注册，则向数据库中插入数据
                User.objects.create(name = username, password = userpwd, create_time="2022-08-27 22:22:22", isdel=0)
                res['rlt'] = '注册成功'
                return render(request, 'accounts/register.html', res)
        elif 'back' in request.POST: #处理返回，界面跳转
            return redirect(request, 'accounts/login.html')
        else:
            pass
    return render(request,'accounts/register.html')

def index(request):
    """
    登录成功
    """
    return render(request,'accounts/index.html')
