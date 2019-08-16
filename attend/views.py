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
                attendlist.clear()
            else:
                # filter condition 

                readtablelist = Attendinfo.objects.all()
                # filter condition
                for index in reversed(attendlist):
                    readtableflag = True
                    for readindex in  readtablelist:          
                        if  index[1] == readindex.attdate and\
                            index[0] == readindex.staffnum and\
                            index[7] == readindex.machine:
                            if index[3] < readindex.starttime:
                                readtableflag = False
                                # return render(request, 'attend/attendence.html',{'attendlist': readtablelist ,'form': form,'test': readindex.id,'test2':12})
                                Attendinfo.objects.filter(id = readindex.id).update(starttime = index[3],verifyS = index[4])
                            if index[5] < readindex.stoptime:
                                readtableflag = False
                                Attendinfo.objects.filter(id = readindex.id).update(stoptime = index[5],verifyT = index[6])                    
                            attendlist.remove(index)                        
                listlen = len(attendlist)
                for index in range(0,listlen):
                    attendlist[index]=Attendinfo(staffnum =attendlist[index][0] ,attdate =attendlist[index][1] ,weekday =attendlist[index][2] ,starttime =attendlist[index][3],
                    verifyS = attendlist[index][4],stoptime =attendlist[index][5] ,verifyT =attendlist[index][6] ,machine =attendlist[index][7] ,hours=attendlist[index][8],
                    )
                Attendinfo.objects.bulk_create(attendlist)
                attendlist.clear()
            readtablelist = Attendinfo.objects.all()
            return render(request, 'attend/attendence.html',{'attendlist':readtablelist,'form': form})
    else:
        form = UploadFileForm()
        if os.path.exists('attend.xls'):
            os.remove('attend.xls')
        if ('exsubmit' in request.GET) or ('queryinfo' in request.GET):
            staffname = request.GET['staffname']
            qstime = request.GET['qstime']
            qetime = request.GET['qetime']
            Mname = request.GET['machinename']
            if  (qstime == '' and qetime != '') or (qstime != '' and qetime == '') or (qstime > qetime):
                return redirect('/attend/')
            else:
                if staffname == '':
                    staffname = '9'
                if Mname == '1':
                    Mname = 'AFCD-03'
                elif Mname == '2':
                    Mname = 'AFCD-04'
                elif Mname == '3':
                    Mname = 'AFCD-05'
                else:
                    Mname = 'AFCD'
                if qstime == '' and qetime == '':
                    readtablelist = Attendinfo.objects.filter(staffnum = int(staffname),machine__icontains = Mname)
                else:
                    readtablelist = Attendinfo.objects.filter(staffnum = int(staffname),attdate__gte = qstime,attdate__lte = qetime,machine__icontains = Mname)
                # if Mname == 'AFCD':
                # return render(request, 'attend/attendence.html',{'attendlist':readtablelist,'form': form})


            # download file
            if 'exsubmit' in request.GET:  
                workbook = xlwt.Workbook(encoding = 'utf-8')
                worksheet = workbook.add_sheet('attenddata')
                worksheet.write(0,0, 'Item')
                worksheet.write(0,1, 'Afnum')
                worksheet.write(0,2, 'Name')
                worksheet.write(0,3, 'Date')
                worksheet.write(0,4, 'weekday')
                worksheet.write(0,5, 'Start Time')
                worksheet.write(0,6, 'verifyS')
                worksheet.write(0,7, 'End Time')
                worksheet.write(0,8, 'verifyE')               
                worksheet.write(0,9, 'Machinename')
                worksheet.write(0,10, 'Hours') 
                i = 0           
                for rindex in reversed(readtablelist):
                    i+=1
                    worksheet.write(i,0,i)
                    worksheet.write(i,1, rindex.staffnum)
                    # worksheet.write(i,2, rindex.)
                    worksheet.write(i,3, rindex.attdate)
                    worksheet.write(i,4, rindex.weekday)
                    worksheet.write(i,5, rindex.starttime)
                    worksheet.write(i,6, rindex.verifyS)
                    worksheet.write(i,7, rindex.stoptime)
                    worksheet.write(i,8, rindex.verifyT)
                    worksheet.write(i,9, rindex.machine)
                    worksheet.write(i,10, rindex.hours)
                workbook.save('attend.xls')
                filedown = open('attend.xls','rb')
                response = FileResponse(filedown)
                response['Content-Type'] = 'application/cetet-stream'
                response['Content-Disposition']='attachment;filename=attend.xls'
                return response
            elif 'queryinfo' in request.GET: 
                return render(request, 'attend/attendence.html',{'attendlist':readtablelist,'form': form})
        else:
            return render(request, 'attend/attendence.html',{'form': form})

def content(request):
    return render(request, 'attend/attendcontent.html')
                        # return render(request, 'attend/attendence.html',{'attendlist': readtablelist ,'form': form,'test': readtablelen,'test2':str(type(readtablelist))})



        
