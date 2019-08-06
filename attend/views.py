from django.shortcuts import render
# my code region
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import xlrd
import xlwt

# my attend function

attendlist = []
def attend(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            data = xlrd.open_workbook(filename=None,file_contents=f.read(), encoding_override='utf-8')
            table = data.sheets()[0]
            nrows = table.nrows
            myrow = nrows-1
            for i in range(1,nrows):
                attendlist.append(table.row_values(i))
                date = attendlist[i-1][0].split(' ')[0]
                time = attendlist[i-1][0].split(' ')[1]
                attendlist[i-1].insert(0,date)
                attendlist[i-1][1]=time
            return render(request, 'test.html',{'attendlist':attendlist,'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'test.html',{'form': form})






        
