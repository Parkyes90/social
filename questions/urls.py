from django.urls import include, path

from rest_framework.routers import DefaultRouter

from questions import views

ROUTER = DefaultRouter()
ROUTER.register(r"questions", views.QuestionViewSet)

urlpatterns = [
    path("", include(ROUTER.urls)),
    path(
        "questions/<slug:slug>/answers/",
        views.AnswerListAPIView.as_view(),
        name="answer-list",
    ),
    path(
        "questions/<slug:slug>/answer/",
        views.AnswerCreateAPIView.as_view(),
        name="create-answer",
    ),
]
