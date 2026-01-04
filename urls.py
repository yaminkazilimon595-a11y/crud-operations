from django.contrib import admin
from django.urls import path
from myapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',studentpage, name='studentpage'),
    path('addstudent/',addstudent, name='addstudent'),
    path('singlestudent/<int:id>/',singlestudent, name='singlestudent'),
    path('updatestudent/<int:id>/',updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>/',deletestudent, name='deletestudent'),
]