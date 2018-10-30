from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def msg(request):
    print('I am runing')
    return HttpResponse('I love SongYue')

def date(request,year,month):
    return HttpResponse('Today is {},{}'.format(year,month))

def dosomething(request):
    return HttpResponse('这是一个子路由')

def msg1(request,pn):
    return HttpResponse('这是第{}页'.format(pn))

def name(request,name):
    return HttpResponse('My name is {}'.format(name))

def reverse1(request):
    return HttpResponse('Your request URL is {}'.format(reverse('askname')))