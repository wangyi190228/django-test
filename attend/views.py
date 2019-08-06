from django.shortcuts import render
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd
import xlwt
from io import StringIO

# my attend function


def attend(request):
    attendlist = []
    templist=[]
    tempflag = False
    if request.method == 'POST':
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
            

            workbook = xlwt.Workbook(encoding = 'utf-8')
            # 创建一个worksheet
            worksheet = workbook.add_sheet('My Worksheet')
            # 写入excel
            # 参数对应 行, 列, 值
            worksheet.write(1,0, label = 'this is test')
            # 保存
            workbook.save('Excel_test.xls')

            return render(request, 'test.html',{'attendlist':attendlist,'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'test.html',{'form': form})





        
