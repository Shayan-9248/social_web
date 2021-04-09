from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.urls import path, include

urlpatterns = [
    path('adm/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret-admin-panel/', admin.site.urls),
    path('', include('core.urls',namespace='core')),
    path('', include('accounts.urls',namespace='account')),
    path('', include('post.urls',namespace='post')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('allauth.urls')),
]

AdminSite.site_header = 'Social Web Admin'
AdminSite.site_title = 'Social Web Administration'
AdminSite.index_title = 'Welcome to Social Web Application'