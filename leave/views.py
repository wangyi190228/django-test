from django.shortcuts import render, redirect

# send mail
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

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
        stop = request.POST['stop']
        day = request.POST['Daysnum']
        if  start == '' or stop == '' or day == '0':
            return redirect('/annual/')
        else:
            # send_mail(
            #     'Remind',
            #     'You have a new message',
            #     '1204534516@qq.com',
            #     ['yi.wang@afconsult.com'],
            #     fail_silently=False,
            # )
            content = {'start':request.POST['start'],'stop':request.POST['stop'],'Daysnum':request.POST['Daysnum']}
            return render(request,str2,content)
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
    if request.is_ajax():
        return render(request, str2)


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




