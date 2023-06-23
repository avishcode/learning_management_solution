from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from courses.models import Course
from memberships.models import Subscription, SubscriptionType
from datetime import datetime, timedelta


# Create your views here.


@login_required
def subscribe(request, course_id, subscription_type_id):
    course = Course.objects.get(id=course_id)
    subscription_type = SubscriptionType.objects.get(id=subscription_type_id)
    end_date = datetime.now().date() + timedelta(days=subscription_type.duration_days)
    subscription = Subscription(user=request.user, course=course, subscription_type=subscription_type, end_date=end_date)
    subscription.save()
    return redirect('courses:course_list')

@login_required
def cancel_subscription(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    subscription.delete()
    return redirect('courses:course_list')