from django.contrib import admin

from .models import (Interview, Question, )

class QuestionInline(admin.TabularInline):
  model = Question

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
  model = Interview
  fields = ('name', 'description', 'date_start', 'date_end', )
  inlines = (QuestionInline, )
  list_display = ('name', 'date_start', 'date_end', )

  def get_readonly_fields(self, request, obj=None):
    if obj:
      return ('date_start', )
    else:
      return ()