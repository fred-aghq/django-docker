import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    body = models.CharField('Question Text', max_length=200)
    published_on = models.DateTimeField('Date Published')

    def __str__(self):
        return self.body

    def wasPublishedRecently(self):
        now = timezone.now();
        return now - datetime.timedelta(days=1) <= self.published_on <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField('Choice Text', max_length=200)
    votes = models.IntegerField('Number of Votes', default=0)

    def __str__(self):
        return self.body

