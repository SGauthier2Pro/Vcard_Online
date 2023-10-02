from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'container-fluid text-center',
                'size': '70%',
                'placeholder': "Nom d'utilisateur"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'container-fluid text-center',
                'size': '70%',
                'placeholder': "Mot de passe"
            }
        )
    )
