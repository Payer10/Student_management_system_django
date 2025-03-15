
from django.urls import path
from .views import*

urlpatterns = [
    path('home',home,name='home'),
    path('',all_student,name="all_student"),
    path('Delete/<int:stu_id>',Delete,name="Delete"),
    path('edit/<int:stu_id>',Edit,name='edit')
]
