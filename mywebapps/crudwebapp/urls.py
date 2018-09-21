"""crudwebapp URL Configuration."""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='department'),
    path('add_department/', views.add_department, name='department add'),
    path(
        'edit_department/<int:department_id>/',
        views.edit_department,
        name='department edit'
    ),
    path(
        'update_department/<int:department_id>',
        views.update_department,
        name='department update'
    ),
    path(
        'delete_department/<int:department_id>/',
        views.delete_department,
        name='department delete'
    ),
    path('employees/', views.employees, name='employee')
]
