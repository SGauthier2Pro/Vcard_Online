from django import forms


class AccessCodeForm(forms.Form):
    access_code_invited = forms.CharField(
        label='access_code',
        max_length=100
    )
