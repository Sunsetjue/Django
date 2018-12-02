from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.views import defaults
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

def notfound(request):
    raise Http404

def get_dic(request):
    rst = ''
    for k,v in request.GET.items():
        rst = rst + k + '- - >' + v
        rst += ','
        return HttpResponse('Get value of Request is {}'.format(rst))

def get_post(request):
    return render_to_response('for_post.html')

def for_post(request):
    rst = ''
    for k,v in request.POST.items():
        rst += k + '- - >' + v
        rst += ','
        return HttpResponse('Get value of Post is {}'.format(rst))

def for_render(request):
    rsp = render(request, 'for_render.html')
    return rsp

def for_render2(request):
    #创造环境变量
    c = dict()
    c['name'] = 'SongYue'
    rsp = render(request, 'for_render2.html',context=c)#context表示联系上下文环境

    '''
    from django.template import loader
    t = loader.get_template('for_render2.html)
    r = t.render({('name':'SongYue')})
    return HttpResponse(r)
    第二种方法
    '''
    return rsp

def get404(request):
    return defaults.page_not_found(request,template_name='404.html')
