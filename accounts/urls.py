from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign-in'),
]