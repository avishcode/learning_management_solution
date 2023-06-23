from django.urls import path
from courses import views
from .views import CourseDetailView


app_name = 'courses'


urlpatterns = [
   path('course_list', views.course_list, name='course_list'),
   # path('course/<int:pk>', views.course_view, name='course_detail'),
   path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
]
