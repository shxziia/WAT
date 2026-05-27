
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('supply_chain/', include('supply_chain.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('search/', views.search, name='search'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='supply_chain/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
