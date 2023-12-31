from django.contrib.auth import get_user_model
from django import forms
from users.models.customuser import CustomUser


class ProfileForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_profile = forms.BooleanField(widget=forms.HiddenInput,
                                      initial=True)

    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'birth_date',
                  'number',
                  'street',
                  'city',
                  'state',
                  'zip_code',
                  'country',
                  'linkedin_url',
                  'git_url',
                  'profile_photo',
                  ]
        widgets = {
            'birth_date': forms.DateInput(format='%Y-%m-%d',
                                          attrs={'type': 'date'}),
            'number': forms.TextInput(attrs={'size': 5}),
            'street': forms.TextInput(attrs={'size': 40}),
            'zip_code': forms.TextInput(attrs={'size': 10}),
            'email': forms.TextInput(attrs={'size': 30}),
            'linkedin_url': forms.TextInput(attrs={'size': 50}),
            'git_url': forms.TextInput(attrs={'size': 50})
        }
