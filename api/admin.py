from django.contrib import admin
from . import models

from django.contrib import admin


# Register your models here.
admin.site.register(models.Grade)
admin.site.register(models.Subject)
admin.site.register(models.Topic)
admin.site.register(models.Question)
admin.site.register(models.QuestionRating)
admin.site.register(models.UserStatistics)
admin.site.register(models.UserAnswer)
admin.site.register(models.AnswerOption)
admin.site.register(models.SubTopics)
