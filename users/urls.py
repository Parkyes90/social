from django.urls import path
from users.views import CurrentUserAPIView

app_name = "users"

urlpatterns = [
    path("users/", CurrentUserAPIView.as_view(), name="current_user")
]
