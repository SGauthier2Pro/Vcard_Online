from django import forms

from skill.models.language import Language


class LanguageForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_language = forms.BooleanField(widget=forms.HiddenInput,
                                       initial=True)

    class Meta:
        model = Language
        fields = [
            'title',
            'level'
        ]


class DeleteLanguageForm(forms.Form):
    delete_language = forms.BooleanField(widget=forms.HiddenInput,
                                         initial=True)
