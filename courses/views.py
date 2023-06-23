from django.shortcuts import render, get_list_or_404
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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



def course_list(request):
    courses = Course.objects.all()
    # subscriptions = Subscription.objects.filter(user=request.user)
    # subscription_types = SubscriptionType.objects.all()
    context = {
        'courses': courses,
        # 'subscriptions': subscriptions,
        # 'subscription_types': subscription_types
    }
    return render(request, 'courses/course_list.html', context)



# @login_required
# def course_view(request, pk):
#     course = get_list_or_404(Course, pk=pk)
#     lessons = course.lesson_set.all()
#     # course_detail = Course.objects.filter(pk=pk)
#     # subscription_types = SubscriptionType.objects.filter(user=request.user)
#     context = {
#         'course':course,
#         'lessons': lessons,
#         # 'subscription_types': subscription_types
#     }
#     return render(request, 'courses/course_view.html', context)

# @login_required
@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_view.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['lessons'] = course.lesson_set.all()
        return context