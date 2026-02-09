from django.db import models


class Question(models.Model):
    """
    Модель вопроса и даты публикации
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    """
    Модель текста варианта ответа и количества голосов.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)