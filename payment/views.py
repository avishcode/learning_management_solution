from django.shortcuts import render, redirect
from django.conf import settings
from razorpay import Client
from .models import Payment

def initiate_payment(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount')) * 100  # Amount in paise
        client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        data = {
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'  # Auto-capture payment after successful payment
        }
        payment = client.order.create(data=data)

        payment_id = payment['id']
        order_id = payment['id']  # Use 'id' instead of 'order_id'
        signature = payment_id + '|' + str(amount)

        Payment.objects.create(amount=amount / 100, razorpay_order_id=order_id, razorpay_payment_id=payment_id, razorpay_signature=signature)

        return redirect('payment:confirm')

    return render(request, 'payment/initiate_payment.html')




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_confirm(request):
    if request.method == 'POST':
        payment = Payment.objects.latest('id')
        client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        params_dict = {
            'razorpay_order_id': payment.razorpay_order_id,
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            payment.status = 'success'
        except:
            payment.status = 'failure'
        
        payment.save()

    return render(request, 'payment/payment_confirm.html')
