from django.urls import reverse, resolve
from django.test import SimpleTestCase
from post.views import (
    PostCreate,
    DeletePost,
    PostDetail,
    PostList,
    UpdatePost,
    post, 
    post_like,
    post_dislike
)

class TestUrls(SimpleTestCase):
    def test_post_create(self):
        url = reverse('post:create')
        self.assertEqual(resolve(url).func.view_class, PostCreate)

    def test_delete_post(self):
        url = reverse('post:delete', args=[7])
        self.assertEqual(resolve(url).func.view_class, DeletePost)

    def test_post_detail(self):
        url = reverse('post:detail', args=['max', 7])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_post_list(self):
        url = reverse('post:list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_update_post(self):
        url = reverse('post:update', args=[7])
        self.assertEqual(resolve(url).func.view_class, UpdatePost)
    
    def test_post(self):
        url = reverse('post:post', args=[7])
        self.assertEqual(resolve(url).func, post)
    
    def test_post_like(self):
        url = reverse('post:like', args=[7])
        self.assertEqual(resolve(url).func, post_like)
    
    def test_post_dislike(self):
        url = reverse('post:dislike', args=[7])
        self.assertEqual(resolve(url).func, post_dislike)