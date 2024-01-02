from django import forms

from portfolio.models.portfolio import Portfolio


class PortfolioForm(forms.ModelForm):

    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Remove: as label suffix

    edit_portfolio = forms.BooleanField(widget=forms.HiddenInput,
                                        initial=True)

    class Meta:
        model = Portfolio
        fields = [
            'title',
            'welcome_sentence',
            'introduction_text',
            'is_visible'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'size': 50})
        }

    def __init__(self, user, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.fields['can_be_display'] = forms.BooleanField(
            widget=forms.CheckboxInput,
            required=False
        )


class DeletePortfolioForm(forms.Form):
    delete_portfolio = forms.BooleanField(widget=forms.HiddenInput,
                                          initial=True)
