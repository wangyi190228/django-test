from django.shortcuts import render
# my code region
from .forms import UploadFileForm

# Create your views here.

# my attend function
# def attend(request):
#     # return render(request, 'attend/attendence.html')
#     if request.method == 'POST':
#         return render(request, 'test.html')
#     else:
#         return render(request, 'test.html')


# def excel_upload(request):
def attend(request):
    '''
    :param request:
    :return: 上传文件excel表格 ,并进行解析
    '''
    if request.method == "POST":
 
        f = request.FILES['my_file']
        type_excel = f.name.split('.')[1]
        if 'xlsx' == type_excel:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
            table = wb.sheets()[0]
            nrows = table.nrows  # 行数
            # ncole = table.ncols  # 列数
            try:
                with transaction.atomic():
                    for i in range(1, nrows):
                        # if 4 == i:
                        #     i/0
                        rowValues = table.row_values(i)  # 一行的数据
                        good = models.GoodsManage.objects.get(international_code=rowValues[0])
                        models.SupplierGoodsManage.objects.create(goods=good, sale_price=rowValues[1],sale_min_count = rowValues[2])
            except Exception as e:
                return JsonResponse({'msg':'出现错误....'})
 
            return JsonResponse({'msg':'ok'})
 
        return JsonResponse({'msg':'上传文件格式不是xlsx'})
 
    return JsonResponse({'msg':'不是post请求'})