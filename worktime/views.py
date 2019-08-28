from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# my work function
@login_required()
def work(request):
    return render(request,'worktime/work.html')


