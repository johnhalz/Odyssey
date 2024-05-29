from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("profile/", views.ManageUserView.as_view(), name="profile"),
    path("login/", views.LoginView.as_view(), name="knox_login"),
    path("logout/", views.LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", views.LogoutAllView.as_view(), name="knox_logoutall"),
]
