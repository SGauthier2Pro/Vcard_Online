from django import forms

from skill.models.softskill import SoftSkill


class SoftSkillForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_softskill = forms.BooleanField(widget=forms.HiddenInput,
                                        initial=True)

    class Meta:
        model = SoftSkill


class DeleteSoftSkillForm(forms.Form):
    delete_softskill = forms.BooleanField(widget=forms.HiddenInput,
                                          initial=True)
