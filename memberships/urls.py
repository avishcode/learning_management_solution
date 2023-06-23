from django.urls import path
from memberships import views

app_name = 'memberships'



urlpatterns = [
    path('subscription_list', views.list_subscriptions, name='subscription_list'),
    path('course/subscribe/<int:course_id>/', views.subscribe, name='subscribe'),
    path('subscription/cancel/<int:subscription_id>/', views.cancel_subscription, name='cancel_subscription'),
]
