from django.urls import path
from . import views

urlpatterns = [
    path('', views.coordinatorPage, name='coordinatorPage'),
    
    path('courses/', views.course, name='course'),
    path('courses/addCourse', views.addCourse, name='addCourse'),
    path('courses/courseRecord/', views.courseRecord, name='courseRecord'),
    path('courses/deleteCourse/<int:id>/', views.deleteCourse, name='deleteCourse'),
    
    path('batches/', views.batch, name='batch'),
]