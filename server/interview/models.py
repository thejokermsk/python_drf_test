from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Interview(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название опроса")
  description = models.TextField(verbose_name="Описание опроса")
  date_start = models.DateTimeField(verbose_name="Дата начала")
  date_end = models.DateTimeField(verbose_name="Дата конца")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "опрос"
    verbose_name_plural = "Опросы"


class Question(models.Model):
  QUESTION_TYPE_CHOICES = [
    ('checkbox', 'Ответ с выбором нескольких вариантов'),
    ('text', 'Ответ текстом'),
    ('radio', 'Ответ с выбором одного варианта'),
  ]

  name = models.CharField(max_length=255, verbose_name="Текст вопроса")
  type = models.CharField(max_length=8, verbose_name="Тип вопроса", choices=QUESTION_TYPE_CHOICES)
  interview = models.ForeignKey(Interview, related_name="questions", verbose_name="Опрос", on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "вопрос"
    verbose_name_plural="Вопросы"


class UserToInterview(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interview')
  interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
  answer = models.CharField(max_length=50)