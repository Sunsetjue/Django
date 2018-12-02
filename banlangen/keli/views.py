from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return render(request,r"2.html")

def two(request):
    # 用来存放向模板中传递的数据
    dt = dict()
    dt['name'] = 'sunbin'
    dt['name'] = 'songyue'
    dt['name1'] = 'sunyuping'
    return render(request,r"3.html",context=dt)

def three(request):
    dt = dict()
    dt['gender'] = [99,110,103,88,94]
    return render(request,r"4.html",context=dt)

def four(request):
    dt=dict()
    dt['age'] = 100
    return render(request,r"5.html",context=dt)