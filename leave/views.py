from django.shortcuts import render, redirect

# from django.http import HttpResponseRedirect
# from .forms import UploadFileForm
# from somewhere import handle_uploaded_file

# Create your views here.

# my annual application function
def annual(request):
    return render(request, 'leave/annual.html')

# my annuallist application function 
def annuallist(request):
    if request.method == "POST":
        start = request.POST['start']
        stop = request.POST['stop']
        day = request.POST['Daysnum']
        if  start == '' or stop == '' or day == '0':
            return redirect('/annual/')
        else:
            request.META['CSRF_COOKIE'] = rotate_token()
            send_mail(
                'Remind',
                'You have a new message',
                '1204534516@qq.com',
                ['yi.wang@afconsult.com'],
                fail_silently=False,
            )
            # content = {'start':request.POST.get('start'),'stop':request.POST.get('stop'),'Daysnum':request.POST.get('Daysnum')}
            content = {'start':request.POST['start'],'stop':request.POST['stop'],'Daysnum':request.POST['Daysnum']}
            return render(request,'leave/annuallist.html',content)
    else:
        return render(request,'leave/annuallist.html')
# my approvallist application function 
def approvallist(request):
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



# send mail
from django.core.mail import send_mail
