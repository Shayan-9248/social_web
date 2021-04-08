from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('account/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('active-mail/<uidb64>/<token>/', views.ActiveEmail.as_view(), name='active-mail'),
    path('log-out/', views.Logout.as_view(), name='log-out'),
    path('dashborad/<int:user_id>/', views.user_dashboard, name='dashboard'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('user-panel/', views.UserPanel.as_view(), name='user-panel'),
    path('change-password/', views.ChangePassword.as_view(), name='change-pass'),
]