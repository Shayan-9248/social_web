from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from rest_framework.authtoken import views

urlpatterns = [
    path('adm/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin/defender/', include('defender.urls')),
    path('secret-admin-panel/', admin.site.urls),
    path('', include('core.urls',namespace='core')),
    path('', include('accounts.urls',namespace='account')),
    path('', include('post.urls',namespace='post')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('allauth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('api/', include('post.api.urls',namespace='post-api')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', views.obtain_auth_token),
]

AdminSite.site_header = 'Social Web Admin'
AdminSite.site_title = 'Social Web Administration'
AdminSite.index_title = 'Welcome to Social Web Application'