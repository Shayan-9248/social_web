# Standard library import
from django.shortcuts import get_object_or_404

# 3rd-party import
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import (
    AuthorAccessPermission,
    IsSuperUserOrStaffOrPermission,
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    PostSerializer,
    UserSerializer,
    CommentCreateSerializer,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from accounts.models import User
from post.models import Post, Comment


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')
    ordering_fields = ('created',)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorAccessPermission, IsAuthenticated)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSuperUserOrStaffOrPermission,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentCreateAPIView(APIView):
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):
        try:
            post = get_object_or_404(Post, id=kwargs.get('id'))
        except Post.DoesNotExist:
            return Response({'Msg': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(post, data=request.data, 
        context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)