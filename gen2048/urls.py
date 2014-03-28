from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'gen2048.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<url>\w+)/$', 'gen2048.views.game', name='game'),
)
