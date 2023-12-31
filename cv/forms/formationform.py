from django import forms

from cv.models.formation import Formation


class FormationForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_formation = forms.BooleanField(widget=forms.HiddenInput,
                                        initial=True)

    class Meta:
        model = Formation
        fields = [
            'title',
            'school_name',
            'location',
            'date_started',
            'date_end',
            'rncp_level',
            'certificate_picture'
        ]
        widgets = {
            'date_started': forms.DateInput(format='%Y-%m-%d',
                                            attrs={'type': 'date'}),
            'date_end': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'type': 'date'}),
        }


class DeleteFormationForm(forms.Form):
    delete_formation = forms.BooleanField(widget=forms.HiddenInput,
                                          initial=True)
