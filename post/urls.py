from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('posts/list/', views.PostList.as_view(), name='list'),
    path('posts/<slug:slug>/<int:id>/', views.PostDetail.as_view(), name='detail'),
]