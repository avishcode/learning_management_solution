from django.db import models

# Create your models here.


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    short_dec = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150)
    category = models.ForeignKey(CourseCategory, on_delete=models.DO_NOTHING)
    long_description = models.TextField(blank=True)
    thumbnail = models.ImageField(blank=True, upload_to="course_thumbnail")

    def __str__(self):
        return self.name
    


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    lesson_file = models.FileField(upload_to="course/lessons")

    def __str__(self):
        return self.name
    
