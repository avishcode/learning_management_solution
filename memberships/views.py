from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from courses.models import Course
from memberships.models import Subscription, SubscriptionType
from datetime import datetime, timedelta
import razorpay

razorpay_client = razorpay.Client(auth=('rzp_test_cqxapLikT85Mpc', '4SjKdTJxoGAOBnX5UQfPWWwg'))


# Create your views here.

def list_subscriptions(request):
    subscriptions = SubscriptionType.objects.all()
    return render(request, "memberships/membership_list.html", {'subscriptions':subscriptions})


@login_required
def subscribe(request, course_id, subscription_type_id):
    course = Course.objects.get(id=course_id)
    subscription_type = SubscriptionType.objects.get(id=subscription_type_id)
    end_date = datetime.now().date() + timedelta(days=subscription_type.duration_days)
    subscription = Subscription(user=request.user, course=course, subscription_type=subscription_type, end_date=end_date)
    subscription.save()

    # Create a Razorpay order
    amount = int(course.price * 100)  # Convert price to paise (Razorpay accepts amount in paise)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': str(subscription.id),
        'payment_capture': 1,
    }
    order = razorpay_client.order.create(data=order_data)

    context = {
        'course': course,
        'subscription': subscription,
        'order_id': order['id'],
        'razorpay_api_key': 'rzp_test_cqxapLikT85Mpc',
    }
    return render(request, 'subscriptions/subscription_confirmation.html', context)



    # return redirect('courses:course_list')

def handle_payment_callback(request):
    # Process the payment callback/notification from Razorpay
    # Verify the callback's authenticity

    # Capture the payment
    payment_id = request.POST.get('payment_id')  # Extract the payment ID from the callback data

    client = razorpay.Client(auth=('YOUR_RAZORPAY_KEY', 'YOUR_RAZORPAY_SECRET'))
    try:
        response = client.payment.capture(payment_id)
        # Payment captured successfully
        # Update your application's data or take any necessary actions
        # ...
    except razorpay.errors.RazorpayError as e:
        # Handle capture failure or errors
        # Log the error, notify the user, or take appropriate actions
        # ...
    
        # Return a response to Razorpay (e.g., HTTP 200 OK)
        return HttpResponse(status=200)




@login_required
def cancel_subscription(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    subscription.delete()
    return redirect('courses:course_list')