from django.shortcuts import render,redirect
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd,xlwt,datetime,os,time
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
                        tempdate = datetime.datetime.strptime(table.row_values(i)[0].split(' ')[0],"%Y-%m-%d").date()            
                        templist.extend([int(table.row_values(i)[1]),tempdate])  
            
                        templist.append(datetime.datetime(tempdate.year,tempdate.month,tempdate.day).strftime("%a"))
                        tempdate = table.row_values(i)[0].split(' ')[1]
                        
                        templist.append(tempdate)
                        templist.extend([table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0.0])
                        attendlist.append([])
                        attendlist[0] = templist.copy()  
                    else:
                        for index in range(0,listlen):
                            tempdate = table.row_values(i)[0].split(' ')[0]
                            tempdate =datetime.datetime.strptime(tempdate, "%Y-%m-%d").date() 
                            temptime = table.row_values(i)[0].split(' ')[1]
                            if tempdate == attendlist[index][1] and int(table.row_values(i)[1]) != attendlist[index][0]:
                                continue
                            elif tempdate == attendlist[index][1] and int(table.row_values(i)[1]) == attendlist[index][0]:
                                tempflag = False
                                if temptime < attendlist[index][3]:
                                    attendlist[index][3] = temptime
                                    attendlist[index][4] = table.row_values(i)[6]
                                    attendlist[index][8] = '%.1f' %(time.strptime(attendlist[index][5],"%H:%M:%S")[3]-time.strptime(temptime,"%H:%M:%S")[3]+\
                                    (time.strptime(attendlist[index][5],"%H:%M:%S")[4]-time.strptime(temptime,"%H:%M:%S")[4])/60)
                                elif temptime > attendlist[index][5]:
                                    attendlist[index][5]= temptime
                                    attendlist[index][6] = table.row_values(i)[6]
                                    attendlist[index][8] = '%.1f' %(time.strptime(temptime,"%H:%M:%S")[3]-time.strptime(attendlist[index][3],"%H:%M:%S")[3]+\
                                    (time.strptime(temptime,"%H:%M:%S")[4]-time.strptime(attendlist[index][3],"%H:%M:%S")[4])/60)
                            elif tempdate != attendlist[index][1]:
                                tempflag = True
                                continue
                        if tempflag:
                            tempdate = table.row_values(i)[0].split(' ')[0]                    
                            templist.extend([int(table.row_values(i)[1]),datetime.datetime.strptime(tempdate, "%Y-%m-%d").date()]) 
                            templist.append(datetime.datetime(int(tempdate.split('-')[0]),int(tempdate.split('-')[1]),int(tempdate.split('-')[2])).strftime("%a"))
                            tempdate = table.row_values(i)[0].split(' ')[1]
                            templist.append(tempdate)
                            templist.extend([table.row_values(i)[6],tempdate,table.row_values(i)[6],table.row_values(i)[4],0.0])
                            attendlist.append([])
                            attendlist[listlen] = templist.copy()

            listlen = len(attendlist)
            readtablelen = Attendinfo.objects.count()
            if readtablelen == 0:    
                for index in range(0,listlen):
                    attendlist[index]=Attendinfo(staffnum =attendlist[index][0] ,attdate =attendlist[index][1] ,weekday =attendlist[index][2] ,starttime =attendlist[index][3],
                    verifyS = attendlist[index][4],stoptime =attendlist[index][5] ,verifyT =attendlist[index][6] ,machine =attendlist[index][7] ,hours=attendlist[index][8],
                    )
                Attendinfo.objects.bulk_create(attendlist)
            else:
                readtablelist = Attendinfo.objects.all()
                listlen = len(attendlist) - 1
                for index in range(listlen,-1,-1):
                    readtableflag = True
                    for readindex in readtablelist:
                        # readtablelist = Attendinfo.objects.all()
                        if attendlist[index][1] == readindex.attdate and\
                           attendlist[index][0] == readindex.staffnum and\
                           attendlist[index][7] == readindex.machine:
                           return render(request, 'attend/attendence.html',{'attendlist': readtablelist ,'form': form,'test': 1})

                           if attendlist[index][3] < readindex.starttime:
                                readtableflag = False
                                readindex.update(starttime = attendlist[index][3],verifyS = attendlist[index][4])

                                # readtablelist[readindex].starttime = attendlist[index][3]
                                # readtablelist[readindex].verifyS = attendlist[index][4]
                           if attendlist[index][5] < readindex.stoptime:
                                readtableflag = False
                                readindex.update(stoptime = attendlist[index][5],verifyT = attendlist[index][6])
                            
                                # readtablelist[readindex].stoptime = attendlist[index][5]
                                # readtablelist[readindex].verifyT = attendlist[index][6]
                    if readtableflag == False:
                        attendlist.pop(index)
                listlen = len(attendlist)
                for index in range(0,listlen):
                    attendlist[index]=Attendinfo(staffnum =attendlist[index][0] ,attdate =attendlist[index][1] ,weekday =attendlist[index][2] ,starttime =attendlist[index][3],
                    verifyS = attendlist[index][4],stoptime =attendlist[index][5] ,verifyT =attendlist[index][6] ,machine =attendlist[index][7] ,hours=attendlist[index][8],
                    )
                Attendinfo.objects.bulk_create(attendlist)
            readtablelist = Attendinfo.objects.all()
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





        
