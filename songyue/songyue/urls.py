from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'songyue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sunbin/', tv.msg),#访问URL，执行函数，得到结果
    url(r'date/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])',tv.date),#正则的一些用法，也就是URL里可以有参数
    url(r'^teacher/',include(teacher_urls)),#创建子路由
    url(r'book/(?:page-(?P<pn>\d+)/)',tv.msg1),#带有参数的URL的用法
    url(r'^name/$',tv.name,{'name':'jiangbaolong'}),#带有字典的用法
    url(r'^reversename/$',tv.reverse1,name='askname'),#URL反向解析
    url(r'^found/$',tv.notfound),#HTTP404的应用
    url(r'get/',tv.get_dic),#GET函数得到request类似字典的键值对的应用
    url(r'^get_post/',tv.get_post),
    url(r'for_post/',tv.for_post),#POST函数的具体应用
    url(r'^for_render/',tv.for_render),#render函数的应用
    url(r'^for_render2/',tv.for_render2),#render函数的应用2
    url(r'get404/',tv.get404),
]
