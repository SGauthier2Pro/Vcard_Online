from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'container-fluid',
             'size': '70%',
             'placeholder': "Nom d'utilisateur"}
        )
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs.update(
            {'class': 'container-fluid',
             'size': '70%',
             'placeholder': 'Mot de passe'}
        )
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget.attrs.update(
            {'class': 'container-fluid',
             'size': '70%',
             'placeholder': 'Confirmer mot de passe'}
        )
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
        help_texts = {
            'username': None,
        }
