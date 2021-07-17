from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign_in'),
    path('account/sign-up/', views.SignUp.as_view(), name='sign_up'),
    path('active-mail/<uidb64>/<token>/', views.ActiveEmail.as_view(), name='active_mail'),
    path('log-out/', views.Logout.as_view(), name='log_out'),
    path('dashborad/<int:user_id>/', views.UserDashboard.as_view(), name='dashboard'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('user-panel/', views.UserPanel.as_view(), name='user_panel'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('change-password/', views.ChangePassword.as_view(), name='change_pass'),
    path('password-reset/', views.PasswordResetView.as_view(), name='reset'),
    path('password-reset-done/', views.PasswordDoneView.as_view(), name='done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordConfirmView.as_view(), name='confirm'),
    path('password-reset-complete/', views.PasswordCompleteView.as_view(), name='complete'),
    path('user-search/', views.search_user, name='search'),
]