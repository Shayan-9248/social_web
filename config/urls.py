from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls',namespace='core')),
    path('', include('accounts.urls',namespace='account')),
    path('', include('post.urls',namespace='post')),
]
