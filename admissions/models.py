from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    studentclass = models.IntegerField()
    rollno = models.IntegerField()
    address = models.CharField(max_length=100)


class teacher(models.Model):

    name = models.CharField(max_length=100)
    exp = models.IntegerField()
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('teach')
