from django.db import models
from memberships.models import SubscriptionType
# Create your models here.


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    short_dec = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    lesson_file = models.FileField(upload_to="course/lessons")

    def __str__(self):
        return f"{self.name} - {self.course}"
    
