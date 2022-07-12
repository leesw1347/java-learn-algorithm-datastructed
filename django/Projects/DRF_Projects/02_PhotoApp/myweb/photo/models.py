from django.db import models


# Create your models here.

# Photo라는 클래스로 사진 모델을 정의한다
class Photo(models.Model):
    title = models.CharField(max_length=50 , name="title")
    author = models.CharField(max_length=50 , name="author")
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
