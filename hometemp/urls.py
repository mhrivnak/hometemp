from django.conf.urls import patterns

urlpatterns = patterns('',
   (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
   (r'^graph/$', 'hometemp.views.graph'),
)
