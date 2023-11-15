from django import forms

from cv.models.hobbies import Hobbies


class HobbiesForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_hobbies = forms.BooleanField(widget=forms.HiddenInput,
                                      initial=True)

    class Meta:
        model = Hobbies
        fields = [
            'title',
            'description'
        ]


class DeleteHobbiesForm(forms.Form):
    delete_hobbies = forms.BooleanField(widget=forms.HiddenInput,
                                        initial=True)
