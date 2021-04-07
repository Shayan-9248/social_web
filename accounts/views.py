from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.http import JsonResponse
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.urls import reverse
from django.views import View
from post.models import Post
from .forms import *
from .models import *


class SignIn(View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
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


class SignUp(View):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'], email=data['email'], password=data['password'])
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user))
            domain = get_current_site(request).domain
            url = reverse('account:active-mail', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            link = 'http://' + domain + url
            email = EmailMessage(
                'Activate your blog account',
                link,
                'shayan.aimoradii@gmail.com',
                [data['email']],
            )
            email.send(fail_silently=False)
            messages.success(request, 'Please confirm your email address to complete the registration', 'success')
            return redirect('account:sign-in')
        return render(request, self.template_name, {'form': form})


class ActiveEmail(View):
    def _make_hash_value(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('account:sign-in')


class Logout(LoginRequiredMixin, View):
    login_url = 'account/sign-in'

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('/')


@login_required(login_url='account:sign-in')
def user_dashboard(request, user_id):
    users = User.objects.filter(id=request.user.id)
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user_id=user.id)
    is_following = False
    relation = Relation.objects.filter(from_user=request.user, to_user=user)
    if relation.exists():
        is_following = True
    context = {
        'user': user, 'posts': posts,
        'is_following': is_following,
    }
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='account:sign-in')
def follow(request, user_id):
    url = request.META.get('HTTP_REFERER')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # user_id = id
        following = get_object_or_404(User, id=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            messages.error(request, 'already following', 'danger')
        else:
            Relation.objects.create(from_user=request.user, to_user=following)
            messages.success(request, f'you following {user}', 'primary')
    return redirect(url)


@login_required(login_url='account:sign-in')
def unfollow(request, user_id):
    url = request.META.get('HTTP_REFERER')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # user_id = id
        following = get_object_or_404(User, id=user_id)
        check_relation = Relation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            check_relation.delete()
            messages.error(request, f'you unfollowing {user}', 'danger')
        else:
            messages.error(request, 'not exists', 'danger')
    return redirect(url)