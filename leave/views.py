import datetime

from django.shortcuts import render, redirect

# send mail
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import staffAl,Alinfo

# Create your views here.
#my leave pages
str3 = 'leave/approvallist.html'
str1 = 'leave/annual.html'
str2 = 'leave/annuallist.html'
str4 = 'leave/annualdays.html'
str5 = 'leave/staffleave.html'

# my annual application function
@login_required()
def annual(request):
    if request.method == "POST":
        start = request.POST['start']
        alstart = request.POST['alstart']
        stop = request.POST['stop']
        alstop = request.POST['alstop']
        day = request.POST['Daysnum']
        alreason = request.POST['alreason']
        if  start == '' or stop == '' or day == '0':
            return redirect('/annual/')
        else:
            nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            obj = Alinfo(starttime=(start+alstart),applicant = "w",
                  stoptime=(stop+alstop),aldays=day, aplitime=nowTime,reason = alreason,status= "submitted")
            obj.save()
            send_mail(
                'New message',
                'You have a new message',
                '1204534516@qq.com',
                ['yi.wang@afconsult.com'],
                fail_silently=False,
            )
        #    datatuple = (
        #    ('Subject', 'Message.', 'from@example.com', ['john@example.com']),
        #    ('Subject', 'Message.', 'from@example.com', ['jane@example.com']),
        #    )
        #    send_mass_mail(datatuple)
            return render(request,str2)
    # get method
    return render(request, str1)


# my overview function  
@login_required()
def overview(request):
        return render(request, 'overview.html')
        #   return render(request, 'leave/sal.html')


# my annualdays function  
@login_required()
def annualdays(request):
    if request.is_ajax():
        return render(request, str4)


# my staffleave function
@login_required()
def staffleave(request):
    if request.is_ajax():
        return render(request, str5)


# my annuallist application function 
@login_required()
def annuallist(request):
    readlist=[]
    if request.is_ajax():
        # Alinfo.objects.filter()
        readlist = Alinfo.objects.all()
        return render(request, str2,{"readlist":readlist})


# my approvallist application function 
@login_required()
def approvallist(request):
    if request.is_ajax():
        return render(request, str3)
    else:
        if request.method == 'POST':
            start = request.POST['start']
            stop = request.POST['stop']
            day = request.POST['Daysnum']
            if  start == '' or stop == '' or day == '0':
                return redirect('/annual/')
            else:
                content = {'start':request.POST['start'],'stop':request.POST['stop'],'Daysnum':request.POST['Daysnum']}
                return render(request,'leave/approvallist.html',content)
        else:
            return render(request,'leave/approvallist.html')

@login_required()
def detail(request):
        return render(request, "leave/detail.html")




