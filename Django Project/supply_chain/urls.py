from django.urls import path
from . import views

app_name = 'supply_chain'

urlpatterns = [
    path('', views.hello_world_index, name='index'),
    path('councils/', views.all_councils, name='council_list'),
    path('projects/', views.all_projects, name='projects_list'),
    path('departments/', views.all_departments, name='department_list'),


    path('councils/<slug:slug>/', views.council_detail, name='council_detail'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('departments/<slug:slug>/', views.department_detail, name='department_detail'),

    path('search/', views.search, name='search'),

]
