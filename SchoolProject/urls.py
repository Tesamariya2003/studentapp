from django.contrib import admin
from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    path('student/', views.studentApi),
    re_path(r'^student/([0-9]+)$', views.studentApi),
    path('admin/', admin.site.urls),
]
