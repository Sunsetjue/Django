from django.conf.urls import include, url
from django.contrib import admin
from keli import views as v
from shuoming import views as vi

urlpatterns = [
    # Examples:
    # url(r'^$', 'banlangen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/',v.one),
    url(r'^two/',v.two),
    url(r'^three/',v.three),
    url(r'^four/',v.four),
    url(r'^sess/',vi.sess),
]
