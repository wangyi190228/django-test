from django.shortcuts import render,redirect
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd,xlwt,datetime,os
from django.http import FileResponse
from .models import attendinfo

weekdaylist = {
    0:'Mon',
    1:'Tue',
    2:'Wed',
    3:'Thu',
    4:'Fri',
    5:'Sat',
    6:'Sun',
}
# my attend function
def attend(request):
    attendlist = []
    templist=[]
    tempdate = ""
    tempflag = False 
    if request.method == 'POST':
        listlen = 0
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            data = xlrd.open_workbook(filename=None,file_contents=f.read(), encoding_override='utf-8')
            table = data.sheets()[0]
            nrows = table.nrows
            for i in range(1,nrows):
                tempflag =True
                templist.clear()
                if table.row_values(i)[1] == '':
                    continue
                else:
                    listlen = len(attendlist)
                    
                    if listlen==0:   
                        tempdate = table.row_values(i)[0].split(' ')[0]                    
                        templist.extend(int(table.row_values(i)[1]),tempdate)                      
                        templist.append(weekdaylist[datetime.date(tempdate.split('-')[0],tempdate.split('-')[1],tempdate.split('-')[2]).weekday()])
                        tempdate = table.row_values(i)[0].split(' ')[1]
                        tempdate = tempdate[0:6]
                        templist.append(tempdate)
                        templist.extend(table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0)
                        attendlist.append(templist)
                    else:
                        for index in range(0,listlen):
                            tempdate = table.row_values(i)[0].split(' ')[0]
                            temptime = table.row_values(i)[0].split(' ')[1]
                            if tempdate == attendlist[index][1] and table.row_values(i)[1] != attendlist[index][0]:
                                continue
                            elif tempdate == attendlist[index][1] and table.row_values(i)[1] == attendlist[index][0]:
                                tempflag = False
                                if temptime < attendlist[index][3]:
                                    attendlist[index][3] = temptime[0:6]
                                elif temptime > attendlist[index][5]:
                                    attendlist[index][5]= temptime[0:6]
                            elif tempdate != attendlist[index][1]:
                                tempflag = True
                                continue
                        if tempflag:
                            tempdate = table.row_values(i)[0].split(' ')[0]                    
                            templist.extend(int(table.row_values(i)[1]),tempdate)                      
                            templist.append(weekdaylist[datetime.date(tempdate.split('-')[0],tempdate.split('-')[1],tempdate.split('-')[2]).weekday()])
                            tempdate = table.row_values(i)[0].split(' ')[1]
                            tempdate = tempdate[0:6]
                            templist.append(tempdate)
                            templist.extend(table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0)
                            attendlist.append(templist)
                        
            attendinfo.objects.bulk_create(templist)
            # listlen = len(attendlist)
            # for index in range((listlen-1),-1,-2):
            #     date = attendlist[index-1][0].split(' ')[0]
            #     time = attendlist[index-1][0].split(' ')[1]
            #     attendlist[index-1].insert(0,date)
            #     attendlist[index-1][1]=time
            #     time = attendlist[index][0].split(' ')[1]
            #     attendlist[index-1].insert(2,time)
            #     attendlist.pop(index)
            return render(request, 'attend/attendence.html',{'attendlist':attendlist,'form': form})
    else:
        # download file
        if 'exsubmit' in request.GET:   

            filedown = open('attend.xls','rb')
            response = FileResponse(filedown)
            response['Content-Type'] = 'application/cetet-stream'
            response['Content-Disposition']='attachment;filename=attend.xls'
            return response
        else:

            form = UploadFileForm()
            return render(request, 'attend/attendence.html',{'form': form})





        
