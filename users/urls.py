from django.urls import path
from users.views import UserProfileDetailView, UserRegisterView, UserLoginView, UserLogoutView, UserProfileUpdateView

app_name = "users"
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/update/", UserProfileUpdateView.as_view(), name="profile-update"),
    path("profile/<str:username>/", UserProfileDetailView.as_view(), name="profile-detail"),
]