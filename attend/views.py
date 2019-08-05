from django.shortcuts import render
# my code region
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
            for i in range(0,nrows):
                attendlist.append(table.row_values(i))
                # content.append(form)
            # content.update(i = table.row_values(i))
            # sheet_name = data.sheet_names()[0]
            # table_name = data.sheet_by_name(sheet_name)
            # nrows = table_name.nrows     
            # ncols = table_name.ncols     
            # content = {'form':form,'test':rowvalue[0]}
            return render(request, 'test.html')#,{'test':attendlist[0][0]}
    else:
        form = UploadFileForm()
        return render(request, 'test.html',{'form': form})

# def attend(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST,request.FILES)
#         if form.is_valid():
#             f = request.FILES['file']
#             f_type = f.name.split('.')[1]
#             if f_type in ['xlsx','xls']:
#                 f_wb = xlrd.open_workbook(filename=None,file_contents=f.chunks())
#                 table = f_wb.sheets()[0]
#                 nrows = table.nrows
#                 for i in range(0,nrows):
#                     rowvalues = table.row_values(i)
#                 content = {'test':rowvalues,'form':form}
#             return render(request, 'test.html',content)#{'test':testlist}
#     else:
#         form = UploadFileForm()
#         return render(request, 'test.html',{'form': form})


# def handle_uploaded_file(f,testlist):
    # with open('afattend.xls', 'wb+') as destination:
        # for chunk in f.chunks():
            # testlist.append(chunk)
            # destination.write(chunk)

# def dealfile(file):
    

# def excel_upload(request):
# def attend(request):
    # if request.method == "POST":
 
    #     f = request.FILES['my_file']
    #     type_excel = f.name.split('.')[1]
    #     if 'xlsx' == type_excel:
    #         # 开始解析上传的excel表格
    #         wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
    #         table = wb.sheets()[0]
    #         nrows = table.nrows  # 行数
    #         # ncole = table.ncols  # 列数
    #         try:
    #             with transaction.atomic():
    #                 for i in range(1, nrows):
    #                     # if 4 == i:
    #                     #     i/0
    #                     rowValues = table.row_values(i)  # 一行的数据
    #                     good = models.GoodsManage.objects.get(international_code=rowValues[0])
    #                     models.SupplierGoodsManage.objects.create(goods=good, sale_price=rowValues[1],sale_min_count = rowValues[2])
    #         except Exception as e:
    #             return JsonResponse({'msg':'出现错误....'})
 
    #         return JsonResponse({'msg':'ok'})
 
    #     return JsonResponse({'msg':'上传文件格式不是xlsx'})
 
    # return JsonResponse({'msg':'不是post请求'})



