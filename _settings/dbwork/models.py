from django.db import models


class Articles(models.Model):
    news_title = models.CharField('Название', max_length=50)
    news_anounsment = models.CharField('Анонс', max_length=250)
    news_escription = models.TextField('Статья', max_length=50)
    news_date = models.DateTimeField('Дата')


    def __str__(self):
        return self.news_title


class news_post(models.Model):
    news_title = models.CharField('Название', max_length=50)
    news_anounsment = models.CharField('Анонс', max_length=250)
    news_escription = models.TextField('Статья', max_length=2500)
    news_date = models.DateTimeField('Дата')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.news_title