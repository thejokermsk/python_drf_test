from rest_framework import (generics, status, )
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)

from django.db.models import F

import datetime

from rest_framework.response import Response

from .serializers import (
  QuestionSerializer,
  InterviewSerializer,
  UserToInterviewSerializer,
  AnswerToInterviewSerializer
)

from .models import (
  Question,
  Interview,
  UserToInterview,
)

class InterviewListAPIView(generics.ListAPIView):
  queryset = Interview.objects.filter(date_end__gte=datetime.date.today())
  serializer_class = InterviewSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, )


class AnswerToInterviewListAPIView(generics.ListAPIView):
  queryset = UserToInterview.objects.filter().prefetch_related('interview', )
  serializer_class = UserToInterviewSerializer
  permission_classes = (IsAuthenticated, )
  
  def list(self, request, *args, **kwargs):

    queryset = self.filter_queryset(self.get_queryset()).filter(user_id=request.user.id)
    data = self.get_serializer(queryset, many=True).data

    

    return Response(data)



class AnswerToInterviewCreateAPIView(generics.CreateAPIView):
  serializer_class = AnswerToInterviewSerializer
  permission_classes = (IsAuthenticated, )

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    instance = UserToInterview.objects.create(user_id=request.user.id, **serializer.data)
    serializer = UserToInterviewSerializer(instance)

    return Response(serializer.data)

    


  