from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# Create your models here.



"""
MEMBERSHIP_TYPE = (
    ('FREE', 'Free'),
    ('BASIC', 'Basic'),
    ('PREMIUM', 'Premium'),
)



class Membership(models.Model):
    membership_type = models.CharField(max_length=50, choices=MEMBERSHIP_TYPE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    validity = models.IntegerField(blank=True, null=True, help_text="How long this membership plan will valid after the course purchase")
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

    
# class Subscription(models.Model):
#     membership = models.ForeignKey(Membership, on_delete=models.DO_NOTHING)
#     is_active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name
    



class UserSubscription(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Membership, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    membership_validity = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.user.username
    
"""


class SubscriptionType(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"