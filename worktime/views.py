from django.shortcuts import render

# Create your views here.

# my work function
def work(request):
    return render(request,'worktime/work.html')


