from rest_framework import serializers
from .models import *

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'answer_text']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['question_status', 'approved', 'topic']
    answer_options = AnswerOptionSerializer(many=True)
    subject = SubjectSerializer(many=True)    