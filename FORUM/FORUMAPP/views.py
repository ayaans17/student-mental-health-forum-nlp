from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Forums, iForum

c=0
# Create your views here.
def hi(req):
    forums=Forums.objects.all()
    return render(req,'FORUMAPP/index.html',{'forums':forums})
def hi2(req):
    if req.method=='POST':
        username=req.POST['user']
        email = req.POST['email']
        passw = req.POST['psw']
        conpass = req.POST['psw-repeat']
        if passw==conpass:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(req,"*Username taken")
            elif User.objects.filter(username=username).exists():
                print("email taken")
                messages.info(req, "*Email taken")
            else:
                user=User.objects.create_user(username=username, email=email, password=passw)
                user.save()
                print("user created")
                return redirect('/login')
        else:
            print("password not matching")
            messages.info(req, "*Password not matching")
        return redirect('/')
    else:
        return render(req,'FORUMAPP/register.html')
def hi3(req):
    if req.method=='POST':
        username=req.POST['user']
        passw = req.POST['psw']
        user=auth.authenticate(username=username, password=passw)
        if user is not None:
            auth.login(req,user)
            return redirect('/index')
        else:
            messages.info(req,'*Invalid Credentials')
            return redirect('/login')

    else:
        return render(req, 'FORUMAPP/login.html')
def logout(req):
    auth.logout(req)
    return redirect('/login')

def forums(req):
    forums = Forums.objects.all()
    return render(req,'FORUMAPP/forums.html',{'forums':forums})
def template(req):
    d=req.GET['d']

    a=auth.get_user(req)
    iforums=iForum.objects.all()
    forums = Forums.objects.all()
    if req.method == 'POST':
        if req.POST.get('post'):
            sav=iForum()
            sav.pc = req.POST.get('post');
            sav.posts = d
            sav.username = a
            sav.save()
    return render(req, 'FORUMAPP/template.html',{'iforum':iforums, 'd':d, 'forums':forums})
def likes(req):
    d = int(req.GET['d'])
    a = req.GET['a']
    c = req.GET['c']
    d = d + 1
    iforums = iForum.objects.all()
    forums = Forums.objects.all()
    f=iForum.objects.get(id=a)
    f.likes=d
    f.save()
    for s in iforums:
        print(s.pc,'0')

    return render(req, 'FORUMAPP/template.html',{'iforum':iforums, 'd':c, 'forums':forums})