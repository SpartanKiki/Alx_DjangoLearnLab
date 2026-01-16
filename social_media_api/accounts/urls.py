from django.urls import path
from .views import register, login, profile, follow_user, unfollow_user

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('profile/', profile),
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
]

