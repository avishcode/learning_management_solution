from django.db import models

# Create your models here.


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    # Add any other fields as per your requirement
