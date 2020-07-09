from rest_framework import serializers

from .models import (Question, Interview, UserToInterview, )

from django.contrib.auth import get_user_model
User = get_user_model()

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ('id', 'name', 'type', )


class InterviewSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(read_only=True, many=True)
  
  class Meta:
    model = Interview
    fields = ('name', 'description', 'date_start', 'date_end', 'questions')


class UserToInterviewSerializer(serializers.ModelSerializer):
  interview = InterviewSerializer()
  class Meta:
    model = UserToInterview
    fields = ('interview', 'answer')


class AnswerToInterviewSerializer(serializers.Serializer):
  interview_id = serializers.PrimaryKeyRelatedField(queryset=Interview.objects.all().only('id'))
  answer = serializers.CharField()