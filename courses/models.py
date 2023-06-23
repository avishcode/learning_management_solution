from django.db import models

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
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
    


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    lesson_file = models.FileField(upload_to="course/lessons")

    def __str__(self):
        return self.name
    
