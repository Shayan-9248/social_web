from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSitemap
from . import views

app_name = 'post'

sitemaps = {
    'static': BlogSitemap,
}


urlpatterns = [
    path('posts/list/', views.PostList.as_view(), name='list'),
    path('posts/<slug:slug>/<int:id>/', views.PostDetail.as_view(), name='detail'),
    path('api/post/<int:pk>/', views.post, name='post'),
    path('post-like/<int:pk>/', views.post_like, name='like'),
    path('post-dislike/<int:pk>/', views.post_dislike, name='dislike'),
    path('post-create/', views.PostCreate.as_view(), name='create'),
    path('post-update/<int:pk>/', views.UpdatePost.as_view(), name='update'),
    path('post-delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
<<<<<<< HEAD
    path('favourite-post/<int:id>/', views.add_to_favourite, name='fav'),
    path('favourite-list/', views.favourite_list, name='fav-list'),
=======
    path('save-post/<int:id>/', views.saved_post, name='save'),
    path('saved-post-list/', views.saved_post_list, name='saved-post'),
>>>>>>> master
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]