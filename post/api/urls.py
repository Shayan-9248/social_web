from django.urls import path
from . import views

app_name = 'post-api'


urlpatterns = [
    path('post/list/', views.PostListAPIView.as_view(), name='list'),
    path('post/detail/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('post/create/', views.PostCreateAPIView.as_view(), name='create'),\
]