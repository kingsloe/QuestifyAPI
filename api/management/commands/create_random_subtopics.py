import faker
import random
from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        fake = faker.Faker()

        topics = models.Topic.objects.all()
        subjects = models.Subject.objects.all()

        for topic in topics:
            for _ in range(2):
                sub_topic_name = fake.word()

                num_subjects_selected = random.choice([1, 2])
                selected_subjects = random.sample(list(subjects), num_subjects_selected)

                sub_topics = models.SubTopics(sub_topic_name=sub_topic_name)
                sub_topics.save()

                sub_topics.subject_name.set(selected_subjects)
                sub_topics.topic_name.add(topic)
                
                # models.SubTopics.objects.bulk_create(subtopics)
        self.stdout.write(self.style.SUCCESS('Sub-topics successfully created'))        
