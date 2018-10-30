from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'songyue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sunbin/', tv.msg),
    url(r'date/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])',tv.date),
    url(r'^teacher/',include(teacher_urls)),
    url(r'book/(?:page-(?P<pn>\d+)/)',tv.msg1),
    url(r'^name/$',tv.name,{'name':'jiangbaolong'}),
    url(r'^reversename/$',tv.reverse1,name='askname'),
]
