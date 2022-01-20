from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 DB에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'users/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)
        
        if password != password2:
            return render(request, 'users/signup.html')
        else:
            user_check = get_user_model().objects.filter(username=username)
            if user_check:
                return render(request, 'users/signup.html')
        
        UserModel.objects.create_user(
            username = username,
            password = password,
            bio = bio
        )
        return redirect('/sign-in')

def sign_in_view(request):
    if request.method =='GET':
        user = request.user.is_authenticated        # 로그인 여부 판단
        if user:
            return redirect('/')
        else:        
            return render(request, 'users/signin.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = auth.authenticate(request, username=username, password=password)   # 계정확인
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')


@login_required         # 로그인상태일경우만 접근 가능.
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def user_view(request):
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'users/user_list.html', {'user_list':user_list})

@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')