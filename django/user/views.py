from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)
        
        if password != password2:
            return render(request, 'users/signup.html')
        else:
            user_check = UserModel.objects.filter(username=username)
            if user_check:
                return render(request, 'users/signup.html')
        
        UserModel.objects.create(
            username = username,
            password = password,
            bio = bio
        )
        return redirect('/sign-in')

def sign_in_view(request):
    if request.method =='GET':
        return render(request, 'users/signin.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return HttpResponse(me.username)
        else:
            return redirect('/sign-in')

        