from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('log-out/', views.Logout.as_view(), name='log-out'),
    path('dashborad/<int:user_id>/', views.user_dashboard, name='dashboard'),
]