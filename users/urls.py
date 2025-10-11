from django.urls import path
from .views import UserProfileView, RegisterView, ProfileView

urlpatterns = [
    # path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
