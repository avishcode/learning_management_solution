from django.urls import path
from courses import views
from .views import *

app_name = 'courses'


urlpatterns = [
   path('course_list', views.course_list, name='course_list'),
]
