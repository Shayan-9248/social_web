from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from .permissions import (
    AuthorAccessPermission,
    IsSuperUserOrStaffOrPermission
)
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    PostSerializer,
    UserSerializer
)
from accounts.models import User
from post.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorAccessPermission, IsAuthenticated)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSuperUserOrStaffOrPermission,)

    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.pk)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer