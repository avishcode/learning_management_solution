from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-confirm/', views.payment_confirm, name='confirm'),
]
