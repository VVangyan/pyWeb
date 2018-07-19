from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#处理post请求
from django.views.decorators.csrf import csrf_exempt,csrf_protect

def index(request):
    context = {}
    context['hello'] = 'Hello World!'  # 数据绑定
    return render(request, 'index.html', context)  # 将绑定的数据传入前台

@csrf_exempt
def hello(req):#注意,此处必须有req 参数否则报错。
    return HttpResponse("hello world")

def user(req):
    #usrname=req.GET.get("username")
    #age=req.GET.get("age")
    #print(usrname,age)
    if req.method=="POST":
        username=req.POST.get("username")
        age=req.POST.get("age")
        print("姓名 ："+ username +"年龄 :"+age)
        return HttpResponse("success")

    return render(req, 'user.html')

