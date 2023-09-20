from django.db import models

class Cheese(models.Model):
    name = models.CharField(max_length=30)
    origin_country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
