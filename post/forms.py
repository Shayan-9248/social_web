from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=70, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))