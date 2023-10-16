from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(QuestionRating)
admin.site.register(UserStatistics)
admin.site.register(UserAnswer)
admin.site.register(AnswerOption)
