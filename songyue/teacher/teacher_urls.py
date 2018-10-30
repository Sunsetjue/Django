from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'songyue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'liuyang/',views.dosomething),
]