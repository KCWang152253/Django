from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(\d+)/$', views.detail),


    url(r'^grades/$', views.grades),
    url(r'^students/$',views.students),


    url(r'^grades/(\d+)$', views.gradesStudents),





    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$',views.showmain),
   # url(r'^quit/$', views.quit),


]