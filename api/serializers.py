from rest_framework import serializers
from . import models

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnswerOption
        fields = ['id', 'answer_text']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ['id', 'subject_name']

class QuestionSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True)
    subject = SubjectSerializer(many=True) 
    class Meta:
        model = models.Question
        exclude = ['question_status', 'topic']
   