from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout


# Create your views here.

# my login function

def aflogin(request):
    alert = False
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')   
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/home/")
        else:
            alert = True
            return render(request, 'login/login.html',{'alert':alert})


# my logout function
def aflogout(request):
    logout(request)
    return render(request, 'login/logout.html')

# my register function
def resetpwd(request):
    return render(request, 'login/resetpwd.html')

@login_required()
def home(request):
      return render(request,'home.html')