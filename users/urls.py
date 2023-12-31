from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

from users.views.signup_page import signup_page
from users.views import edit_profile


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='users/password_change_form.html',
        success_url=reverse_lazy('users:password_change_done')),
        name='password_change'
        ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', signup_page, name='signup'),
    path('edit-profile/', edit_profile.edit_profile,
         name='edit_profile'),
    path('profile/', edit_profile.index, name='profile_home'),
    path('generate-guest-access/', edit_profile.generate_guest_access_code,
         name='generate_guest_access_code'),
]
