from django import forms

from cv.models.experience import Experience
from cv.models.hobbies import Hobbies
from cv.models.formation import Formation

from skill.models.technology import Technology
from skill.models.softskill import SoftSkill
from skill.models.language import Language

from cv.models.cv import Cv


class CvForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_cv = forms.BooleanField(widget=forms.HiddenInput,
                                 initial=True)

    class Meta:
        model = Cv
        fields = [
            'title',
            'profil',
            'experiences',
            'languages',
            'technologies',
            'softskills',
            'hobbies',
            'formations',
            'can_be_display'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'size': 50})
        }

    def __init__(self, user, *args, **kwargs):
        super(CvForm, self).__init__(*args, **kwargs)
        self.fields['technologies'] = forms.ModelMultipleChoiceField(
            queryset=Technology.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['softskills']=forms.ModelMultipleChoiceField(
            queryset=SoftSkill.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['experiences'] = forms.ModelMultipleChoiceField(
            queryset=Experience.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['languages'] = forms.ModelMultipleChoiceField(
            queryset=Language.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['hobbies'] = forms.ModelMultipleChoiceField(
            queryset=Hobbies.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['formations'] = forms.ModelMultipleChoiceField(
            queryset=Formation.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['can_be_display'] = forms.BooleanField(
            widget=forms.CheckboxInput,
            required=False
        )


class DeleteCvForm(forms.Form):
    delete_cv = forms.BooleanField(widget=forms.HiddenInput,
                                   initial=True)
