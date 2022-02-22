from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .views import changepassword

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutpage, name='logout'),

    path('password_change/', changepassword.as_view(template_name='authe/password_change.html'), name="password_change"),
    path('password_change_successful/', views.changesuccessful, name='change_successful'),

    # should be moved to task
    path('', views.home, name='home'),

    #password reset 
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='authe/password_reset.html'),
    name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='authe/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authe/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authe/password_reset_done.html'), name='password_reset_complete'),
    
]