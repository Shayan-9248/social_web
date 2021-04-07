from django import forms
from .models import User


message = {
    'invalid': 'Please enter a valid email address',
    'required': 'This field is required',
    'max_length': 'Carachter for this field is too long'
}


class SignInForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.TextInput())
    password = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.PasswordInput())
    remember = forms.CharField(required=False, label='Remember Me', widget=forms.CheckboxInput())


class SignUpForm(forms.Form):
    username = forms.CharField(error_messages=message, max_length=70, widget=forms.TextInput())
    email = forms.EmailField(error_messages=message, max_length=70, widget=forms.TextInput())
    password = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.PasswordInput())
    confirm_password = forms.CharField(error_messages={'required': 'This field is required'}, widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('This username is already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('This email address is already exists')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match!')
        return confirm_password