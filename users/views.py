from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.


def index(request):
    # if request.method == 'POST':
    #     img = request.FILES.get('commodityImage')
    #     img_name = img.name
    #     path = os.path.join('C://', '图片')
    #     if not os.path.isdir(path):
    #         os.mkdir(path)
    #     path_img = os.path.join(path, img_name)
    #     with open(path_img, 'wb+') as f:
    #         for i in img:
    #             f.write(i)
    #     return HttpResponse('上传成功...')
    # else:
    return render(request, 'index.html')