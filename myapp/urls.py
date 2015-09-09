from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
#admin.autodiscover()


    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog', 'blog.views.post_form_upload', name='blog'),
    url(r'^post/form_upload.html$',
        'blog.views.post_form_upload', name='post_form_upload'),
    url(r'^up', 'blog.views.up', name='up'),
    url(r'^delete/(?P<id>\d+)$', 'blog.views.delete', name='delete'),
    url(r'^edit/(?P<id>\d+)$', 'blog.views.edit', name='edit')

)

