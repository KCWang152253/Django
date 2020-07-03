from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$', views.detail),


    url(r'^grades/$', views.grades),
    url(r'^students/$',views.students),
    url(r'^students2/$',views.students2),
    url(r'^students3/$',views.students3),
    url(r'^stu/(\d+)/$',views.stupage),
    url(r'^studentsearch/$',views.studentsearch),
    url(r'^grades/$',views.grades),



    url(r'^addstudent/$', views.addstudent),
    url(r'^addstudent2/$', views.addstudent2),

    url(r'^grades/(\d+)$', views.gradesStudents),



    url(r'^attribles', views.attribles),
    url(r'^get1$', views.get1),
    url(r'^get2$', views.get2),
    url(r'^showregist/$',views.showregist),
    url(r'^showregist/regist/$',views.regist),
    url(r'^showresponse',views.showresponse),
    url(r'^cookietest',views.cookietest),
    url(r'^redirect1',views.redirect1),
    url(r'^redirect2',views.redirect2),

    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$', views.quit),



    url(r'^verifycode/$',views.verifycode),
    url(r'^verifycodefile/$',views.verifycodefile),
    url(r'^verifycodecheck/$',views.verifycodecheck),




    # url(r'^set_session$', views.set_session),           # 保存session数据
    # url(r'^get_session$', views.get_session),
    # url(r'^get1/$', views.get1),
]