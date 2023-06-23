from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Course
from memberships.models import Subscription, SubscriptionType



# Create your views here.
"""
def list_courses(request):
    courses = Course.objects.all()
    return render(request, "courses/display_courses.html", {'courses':courses})

class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/add_courses.html"
    fields = '__all__'
    success_url = reverse_lazy('courses:list-courses')
"""


@login_required
def course_list(request):
    courses = Course.objects.all()
    subscriptions = Subscription.objects.filter(user=request.user)
    subscription_types = SubscriptionType.objects.all()
    context = {
        'courses': courses,
        'subscriptions': subscriptions,
        'subscription_types': subscription_types
    }
    return render(request, 'courses/course_list.html', context)
