from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grade(models.Model):
    grade_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.grade_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=150, null=True)
    grade = models.ManyToManyField(Grade)

    def __str__(self):
        return self.subject_name

class Topic(models.Model):
    topic_name = models.CharField(max_length=150, null=True)
    subjects = models.ManyToManyField('Subject', related_name='topics')

    def __str__(self):
        return self.topic_name


class Question(models.Model):
    QUESTION_TYPE = [
        ('two_choices', 'True or False'),
        ('multiple_choices', 'MULTIPLE CHOICE')
    ]

    STATUS = [
        ('pending', 'PENDING'),
        ('active', 'ACTIVE'),
        ('archived', 'ARCHIVED'),
    ]

    subject = models.ManyToManyField(Subject) 
    topic = models.ManyToManyField(Topic)
    question_type = models.CharField(max_length=150, choices=QUESTION_TYPE, null=True)
    question_text = models.TextField(null=True)
    highlight = models.TextField(null=True)
    approved = models.BooleanField(default=False)
    correct_answer = models.CharField(max_length=200, null=True)
    explanation = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question_status = models.CharField(max_length=150, choices=STATUS)
    diagram_image = models.ImageField(upload_to='images/', null=True, blank=True)
    user_ratings = models.ManyToManyField(User, through='QuestionRating')
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.question_text  
    
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_option')
    answer_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_text

class QuestionRating(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

class UserStatistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questions_created = models.PositiveIntegerField(default=0)
    questions_answered = models.PositiveIntegerField(default=0)
    ratings_given = models.PositiveIntegerField(default=0)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_answer = models.CharField(max_length=200)