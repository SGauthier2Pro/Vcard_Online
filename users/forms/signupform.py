from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Nom d'utilisateur :"

        self.fields['password1'].label = 'Mot de passe :'
        self.fields['password1'].help_text = ''

        self.fields['password2'].label = 'Confirmer mot de passe :'
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
