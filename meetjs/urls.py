from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meetjs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'quiz.views.question', name='question'),
    url(r'^login/$', 'meetjs.views.login', name='login'),
    url(r'^thanks/$', 'quiz.views.thanks', name='thanks'),
)
