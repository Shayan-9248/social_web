from django.shortcuts import render, get_object_or_404
from django.views import View
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
        return render(request, self.template_name, {'post': post})