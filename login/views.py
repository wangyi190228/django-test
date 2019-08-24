from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

# my login function

def aflogin(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')   
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('login:home'))
        else:
            return render(request, 'login/login.html', {
                'username': username,
                'password': password,
            })

# my logout function
def logout(request):
    return render(request, 'login/logout.html')

# my register function
def resetpwd(request):
    return render(request, 'login/resetpwd.html')

@login_required(login_url='/login/')
def home(request):
      return render(request,'home.html')