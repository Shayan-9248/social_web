from django import forms


message = {
    'invalid': 'Please enter a valid email address',
    'required': 'This field is required',
    'max_length': 'Carachter for this field is too long'
}


class SignInForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.TextInput())
    password = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.PasswordInput())
    remember = forms.CharField(required=False, label='Remember Me', widget=forms.CheckboxInput())