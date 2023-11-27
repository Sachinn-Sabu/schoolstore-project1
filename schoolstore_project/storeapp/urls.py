from django.urls import path
from . import views

app_name = 'storeapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('allDept/', views.allDept, name='all_dept'),
    path('allDept/<slug:d_slug>/', views.allDept, name='courses_by_departments'),
    path('user/', views.user, name='user'),
    path('form', views.form, name='form'),
    path('confirm', views.confirm, name='confirm'),
    path('get_courses_by_department/', views.get_courses_by_department, name='get_courses_by_department'),
]
