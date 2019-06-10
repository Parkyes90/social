from django.contrib.auth import get_user_model
from django.db import models

from core.models import TimeStampedModel


class Question(TimeStampedModel):
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return self.content


class Answer(TimeStampedModel):
    body = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answer"
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    voters = models.ManyToManyField(get_user_model(), related_name="votes")

    def __str__(self):
        return self.question.content
