from django.contrib.auth import get_user_model
from django import forms


class ProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name',
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
                  'guest_access_code',
                  'linkedin_url',
                  'profile_photo',
                  )
