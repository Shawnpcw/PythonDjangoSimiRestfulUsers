
from django.conf.urls import url
from . import views         
urlpatterns = [
    url(r'^users$', views.index)  ,
    url(r'^users/(?P<id>\d+)/$', views.expanded)  ,
    url(r'^users/add$', views.adduser)  ,
    url(r'^users/updater/(?P<id>\d+)$', views.updater)  ,
    url(r'^create_process/$', views.create_process)  ,
    url(r'^users/delete/(?P<id>\d+)$', views.delete)  ,
    url(r'^users/create_process/$', views.create_process)  ,
    url(r'^users/(?P<id>\d+)/edit$', views.edituser)  
]                       