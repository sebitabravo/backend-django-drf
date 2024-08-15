from django.db import models


class programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
