from django.shortcuts import render

# Create your views here.

# my login function
def login(request):
    # if request.method == 'post':
    #     username=requset.get('username')
    return render(request, 'login/login.html')

# my logout function
def logout(request):
    return render(request, 'login/logout.html')

# my register function
def register(request):
    return render(request, 'login/register.html')
