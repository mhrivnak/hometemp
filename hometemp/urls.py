from django.conf.urls import patterns

urlpatterns = patterns('',
   (r'^graph/$', 'hometemp.views.graph'),
)
