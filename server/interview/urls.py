from django.urls import path

from .views import (
  InterviewListAPIView,
  AnswerToInterviewListAPIView,
  AnswerToInterviewCreateAPIView
)

urlpatterns = [
  path('', InterviewListAPIView.as_view()),
  path('answer', AnswerToInterviewListAPIView.as_view()),
  path('answer/create', AnswerToInterviewCreateAPIView.as_view()),
]