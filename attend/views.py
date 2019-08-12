from django.shortcuts import render,redirect
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd,xlwt,datetime,os
from django.http import FileResponse
from .models import Attendinfo
# my attend function
def attend(request):
    attendlist = []
    readtablelist = []
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
                        templist.extend([int(table.row_values(i)[1]),tempdate])                      
                        templist.append(datetime.datetime(int(tempdate.split('-')[0]),int(tempdate.split('-')[1]),int(tempdate.split('-')[2])).strftime("%a"))
                        tempdate = table.row_values(i)[0].split(' ')[1]
                        templist.append(tempdate)
                        templist.extend([table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0])
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
                                    attendlist[index][3] = temptime
                                    attendlist[index][4] = table.row_values(i)[6]
                                elif temptime > attendlist[index][5]:
                                    attendlist[index][5]= temptime
                                    attendlist[index][6] = table.row_values(i)[6]
                            elif tempdate != attendlist[index][1]:
                                tempflag = True
                                continue
                        if tempflag:
                            tempdate = table.row_values(i)[0].split(' ')[0]                    
                            templist.extend([int(table.row_values(i)[1]),tempdate]) 
                            templist.append(datetime.datetime(int(tempdate.split('-')[0]),int(tempdate.split('-')[1]),int(tempdate.split('-')[2])).strftime("%a"))
                            tempdate = table.row_values(i)[0].split(' ')[1]
                            templist.append(tempdate)
                            templist.extend([table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0])
                            attendlist.append(templist)


            readtablelen = Attendinfo.objects.count()
            if readtablelen == 0:     
                Attendinfo.objects.bulk_create(attendlist)
            else:
                readtablelist = Attendinfo.objects.all()
                listlen = len(attendlist)
                for index in range(0,listlen):
                    readtableflag = True
                    for readindex in range(0,readtablelen):
                        if attendlist[index][1] == readtablelist[readindex][1] and\
                           attendlist[index][0] == readtablelist[readindex][0] and\
                           attendlist[index][7] == readtablelist[readindex][7]:
                           if attendlist[index][3] < readtablelist[readindex][3]:
                                readtableflag = False
                                readtablelist[readindex][3] = attendlist[index][3]
                                readtablelist[readindex][4] = attendlist[index][4]
                           if attendlist[index][5] < readtablelist[readindex][5]:
                                readtableflag = False
                                readtablelist[readindex][5] = attendlist[index][5]
                                readtablelist[readindex][6] = attendlist[index][6]
                    if readtableflag:
                        readtablelist.append(attendlist[index])    
            return render(request, 'attend/attendence.html',{'attendlist':readtablelist,'form': form})
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





        
