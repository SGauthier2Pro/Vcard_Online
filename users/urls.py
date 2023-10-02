from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

from users.views.signup_page import signup_page
from users.views.upload_profile_photo import upload_profile_photo


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='users/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', signup_page, name='signup'),
    path('profile-photo/upload', upload_profile_photo,
         name='upload_profile_photo'),
]
