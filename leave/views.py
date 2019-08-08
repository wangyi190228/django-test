from django.shortcuts import render, redirect

# send mail
from django.core.mail import send_mail

# Create your views here.
# str1 = 'leave/annual.html'
str3 = 'leave/approvallist.html'
str1 = 'leave/annual.html'
str2 = 'leave/annuallist.html'
str4 = 'leave/annualdays.html'
# str2 = 'test.html'
# my annual application function

def annual(request):
    return render(request, str1)

def overview(request):
    return render(request, 'overview.html')

def annualdays(request):
    if request.is_ajax():
        return render(request, str4)
    else:
        return render(request, str1)

# my annuallist application function 
def annuallist(request):
    if request.is_ajax():
        return render(request, str2)
    else:

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
                # content = {'start':request.POST.get('start'),'stop':request.POST.get('stop'),'Daysnum':request.POST.get('Daysnum')}
                content = {'start':request.POST['start'],'stop':request.POST['stop'],'Daysnum':request.POST['Daysnum']}
                return render(request,str2,content)
        else:
            return render(request,str2)


# my approvallist application function 
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
                # content = {'start':request.POST.get('start'),'stop':request.POST.get('stop'),'Daysnum':request.POST.get('Daysnum')}
                content = {'start':request.POST['start'],'stop':request.POST['stop'],'Daysnum':request.POST['Daysnum']}
                return render(request,'leave/approvallist.html',content)
        else:
            return render(request,'leave/approvallist.html')




