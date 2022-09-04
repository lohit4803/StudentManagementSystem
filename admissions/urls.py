from django.urls import path

from admissions.views import *

from django.contrib.auth.decorators import login_required

urlpatterns=[



path('adad/',addadmission),
path('admrep/',admissionsreport),
path('advendor/',addvendor),
path('del/<int:id>/',deletestudent),
path('upd/<int:id>',updatetable),


path('clsview/',login_required(FirstClassView.as_view())),
path( 'tchr/' , login_required(teacherread.as_view()) , name = 'teach'),
path('tchr1/<int:pk>/',login_required(teacherread1.as_view())),
path('tchr2/',login_required(teachercreate.as_view())),
path('tchr3/<int:pk>/',login_required(teacherupdate.as_view())),
path('tchr4/<int:pk>/',login_required(deleteteacher.as_view())),




]
