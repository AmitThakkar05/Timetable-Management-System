from django.db import models

# Create your models here.
class courseTable(models.Model):
    courseID = models.CharField(max_length=5)
    courseName = models.CharField(max_length=255)
    credit = models.CharField(max_length=5)
    batch = models.CharField(max_length=10)
