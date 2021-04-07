from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Post


class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super().form_valid(form)


class UserAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user == post.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('You are not the owner of this post')