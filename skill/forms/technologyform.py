from django import forms

from skill.models.technology import Technology


class TechnologyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove : as label suffix

    edit_technology = forms.BooleanField(widget=forms.HiddenInput,
                                         initial=True)

    class Meta:
        model = Technology
        fields = [
            'title',
            'level',
            'image'
        ]


class DeleteTechnologyForm(forms.Form):
    delete_technology = forms.BooleanField(widget=forms.HiddenInput,
                                           initial=True)
