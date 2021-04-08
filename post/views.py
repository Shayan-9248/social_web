from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from .mixins import (
    FormValidMixin,
    UserAccessMixin
)
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.urls import reverse_lazy
from .models import *


class PostList(View):
    template_name = 'post/list.html'

    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})


class PostDetail(View):
    template_name = 'post/detail.html'

    def get(self, request, slug, id):
        post = get_object_or_404(Post, slug=slug, id=id)
        ip_address = request.user.ip_address
        if ip_address not in post.visit_count.all():
            post.visit_count.add(ip_address)
        return render(request, self.template_name, {'post': post})


def post(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    return JsonResponse({
        'like': post.like.count(),
        'dislike': post.dislike.count(),
        'status': request.user.is_authenticated
    })


def post_like(request, pk):
    url = request.META.get("HTTP_REFERER")
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if user in post.dislike.all():
        post.dislike.remove(user)
        post.like.add(user)
    elif user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect(url)


def post_dislike(request, pk):
    url = request.META.get("HTTP_REFERER")
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if user in post.like.all():
        post.like.remove(user)
        post.dislike.add(user)
    elif user in post.dislike.all():
        post.dislike.remove(user)
    else:
        post.dislike.add(user)
    return redirect(url)


class PostCreate(FormValidMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'post/create.html'
    login_url = 'account:sign-in'
    model = Post
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('post:list')
    success_message = 'Post created successfully'


class UpdatePost(FormValidMixin, UserAccessMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'post/update.html'
    login_url = 'account:sign-in'
    model = Post
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('post:list')
    success_message = 'Post updated successfully'


class DeletePost(UserAccessMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'post/delete.html'
    ogin_url = 'account:sign-in'
    model = Post
    success_url = reverse_lazy('post:list')
    success_message = 'Post deleted successfully'