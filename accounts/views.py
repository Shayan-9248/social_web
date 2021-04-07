from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from post.models import Post
from .forms import *
from .models import *


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


class Logout(LoginRequiredMixin, View):
    login_url = 'account/sign-in'

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('/')


@login_required(login_url='account:sign-in')
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user_id=user.id)
    is_following = False
    relation = Relation.objects.filter(from_user=request.user, to_user=user)
    if relation.exists():
        is_following = True
    context = {
        'user': user, 'posts': posts,
        'is_following': is_following
    }
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='account:sign-in')
def follow(request, user_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        # user_id = user_id
        following = get_object_or_404(User, user_id=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            messages.error(request, 'already following', 'danger')
        else:
            Relation.objects.create(from_user=request.user, to_user=following)
            messages.error(request, 'following', 'danger')
    return redirect(url)


@login_required(login_url='account:sign-in')
def unfollow(request, user_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        # user_id = user_id
        following = get_object_or_404(User, user_id=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if check_relation.exists():
            check_relation.delete()
            messages.error(request, 'Unfollowing', 'primary')
        else:
            messages.error(request, 'not exists', 'danger')
    return redirect(url)