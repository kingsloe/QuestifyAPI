import faker
from lorem_text import lorem
import random
from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = faker.Faker()
        lorem_question = lorem.words(10)
        grades = models.Grade.objects.all()
        sub_topics = models.SubTopics.objects.all()

        for sub_topic in sub_topics:
            for _ in range(2):
                grade = random.choice(grades)
                subject = sub_topic.subject_name.all().first()
                topic = sub_topic.topic_name.all().first()

                question = models.Question(
                    question_text = lorem_question,
                    correct_answer = fake.word(),
                    explanation = lorem_question,
                    question_status = random.choice(['active', 'pending', 'archived'])
                )
                question.save()
                question.grade.add(grade)  # Add the grade
                question.subject.add(subject)  # Add the subject
                question.topic.add(topic)  # Add the topic
                question.sub_topic.add(sub_topic)  # Add the sub_topic
                self.stdout.write(self.style.SUCCESS('Questions generated questions.'))
