from django.db import models

class Visit(models.Model):
    name = models.TextField()
    address= models.TextField()