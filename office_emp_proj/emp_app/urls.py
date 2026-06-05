from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('home/', views.index, name='index'),
    
    
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
]
