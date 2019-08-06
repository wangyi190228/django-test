from django.shortcuts import render
# my code region
from django.http import HttpResponseRedirect
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
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        content = {'test': request.FILES['file']}
            # return HttpResponseRedirect('/attend/')
        return render(request, 'attend/attendence.html',content)
    else:
        form = UploadFileForm()
    # return render(request, 'attend/attendence.html', {'form': form})
    return render(request, 'attend/attendence.html', {'form': form})
    # return render(request, 'attend/attendence.html')


def handle_uploaded_file(f):
    with open('numtest.xls', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)






        