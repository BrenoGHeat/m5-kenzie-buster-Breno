from django.urls import path
from users.views import UserView
from rest_framework_simplejwt import views
from users.views import UserOwnerView


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
    path("users/login/refresh", views.TokenRefreshView.as_view()),
    path("users/<int:user_id>/", UserOwnerView.as_view())
]
