import datetime

from django.db import models
from django.utils import timezone

from django.http import HttpRequest

#from requests import request


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class MockingExample():

    name = 'T'

    def example(self):
        pass

    def example_call(self):
        self.example()

    def _get_page(self, url):
        return self.request(url)

    def name_in_page(self, url, name):
        resp = self._get_page(url)
        resp.close()
        return self.name in str(resp.content)
