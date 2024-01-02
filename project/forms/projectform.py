from django import forms

from skill.models.technology import Technology
from skill.models.softskill import SoftSkill
from project.models.project import Project


class ProjectForm(forms.ModelForm):
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_project = forms.BooleanField(widget=forms.HiddenInput,
                                      initial=True)

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'date_started',
            'date_end',
            'technologies',
            'softskills',
            'tasks',
            'link_git',
            'presentation_file',
            'image',
            'documents',
            'can_be_display'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'size': 40}),
            'link_git': forms.TextInput(attrs={'size': 55}),
            'date_started': forms.DateInput(format='%Y-%m-%d',
                                            attrs={'type': 'date'}),
            'date_end': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['technologies'] = forms.ModelMultipleChoiceField(
            queryset=Technology.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['softskills'] = forms.ModelMultipleChoiceField(
            queryset=SoftSkill.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple
        )
        self.fields['can_be_display'] = forms.BooleanField(
            widget=forms.CheckboxInput,
            required=False
        )


class DeleteProjectForm(forms.Form):
    delete_project = forms.BooleanField(widget=forms.HiddenInput,
                                        initial=True)
