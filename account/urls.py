from django.urls import path

from account.views import UserCreateView, UserProfileView, CustomLoginView, CustomLogoutView, CustomPasswordChangeView

app_name = 'account'

urlpatterns = [
    path('inscription/', UserCreateView.as_view(), name='signup'),
    path('edition-profil/', UserProfileView.as_view(), name='profile'),
    path('connexion/', CustomLoginView.as_view(), name='login'),
    path('deconnexion/', CustomLogoutView.as_view(), name='logout'),
    path('update-password/', CustomPasswordChangeView.as_view(), name='password-change'),
]
