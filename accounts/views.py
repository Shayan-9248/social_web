from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import *


class SignIn(View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            remember = form.cleaned_data['remember']
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(68400)
                return redirect('/')
            else:
                form.add_error('username', 'username or password is incorrect')
        return render(request, self.template_name, {'form': form})