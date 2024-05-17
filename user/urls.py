from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns =[
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='job_seeker_page/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.job_seeker_profile, name='job-seeker-profile'),
    path('applications', views.user_applications, name='applications-index'),
]