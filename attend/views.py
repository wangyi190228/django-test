from django.shortcuts import render,redirect
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd,xlwt,datetime,os
from django.http import FileResponse
# my attend function
def attend(request):
    attendlist = []
    templist=[]
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
                templist.append(table.row_values(i))
                if templist[0][1] == '':
                    continue
                else:
                    listlen = len(attendlist)
                    if listlen==0:
                        attendlist.append(table.row_values(i))
                        attendlist.append(table.row_values(i))
                    else:
                        for index in range(0,listlen,2):
                            if templist[0][0].split(' ')[0] == attendlist[index][0].split(' ')[0] and templist[0][1] != attendlist[index][1]:
                                continue
                            elif templist[0][0].split(' ')[0] == attendlist[index][0].split(' ')[0] and templist[0][1] == attendlist[index][1]:
                                tempflag = False
                                if templist[0][0] < attendlist[index][0]:
                                    attendlist[index] = templist[0]
                                elif templist[0][0] > attendlist[index+1][0]:
                                    attendlist[index+1] = templist[0]
                            elif templist[0][0].split(' ')[0] != attendlist[index][0].split(' ')[0]:
                                tempflag = True
                                continue
                        if tempflag:
                            attendlist.append(table.row_values(i))
                            attendlist.append(table.row_values(i))
                            
            listlen = len(attendlist)
            for index in range((listlen-1),-1,-2):
                date = attendlist[index-1][0].split(' ')[0]
                time = attendlist[index-1][0].split(' ')[1]
                attendlist[index-1].insert(0,date)
                attendlist[index-1][1]=time
                time = attendlist[index][0].split(' ')[1]
                attendlist[index-1].insert(2,time)
                attendlist.pop(index)
            listlen = len(attendlist) + 1
            workbook = xlwt.Workbook(encoding = 'utf-8')
            # 创建一个worksheet
            worksheet = workbook.add_sheet('My Worksheet')
            # 写入excel
            # 参数对应 行, 列, 值
            worksheet.write(0,0, 'Item')
            worksheet.write(0,1, 'Date')
            worksheet.write(0,2, 'Start Time')
            worksheet.write(0,3, 'End Time')
            worksheet.write(0,4, 'Afnumofperson')
            worksheet.write(0,5, 'Name')
            worksheet.write(0,6, 'Cardnum')
            worksheet.write(0,7, 'Machinename')
            worksheet.write(0,8, 'Event Place')
            worksheet.write(0,9, 'Verify')
            worksheet.write(0,10, 'Status')
            worksheet.write(0,11, 'Type')
            worksheet.write(0,12, 'Backup')
            for rindex in range(1,listlen):
                worksheet.write(rindex,0,rindex)
                for cindex in range(1,13):
                    worksheet.write(rindex,cindex, attendlist[rindex-1][cindex-1])
            # 保存
            workbook.save('attend.xls')
            return render(request, 'test.html',{'attendlist':attendlist,'form': form})
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
            return render(request, 'test.html',{'form': form})





        
