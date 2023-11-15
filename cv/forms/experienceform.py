from django import forms

from cv.models.experience import Experience


class ExperienceForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_experience = forms.BooleanField(widget=forms.HiddenInput,
                                         initial=True)

    class Meta:
        model = Experience
        fields = [
            'title',
            'company_name',
            'location',
            'date_started',
            'date_end',
            'tasks',
        ]


class DeleteExperienceForm(forms.Form):
    delete_experience = forms.BooleanField(widget=forms.HiddenInput,
                                           initial=True)
