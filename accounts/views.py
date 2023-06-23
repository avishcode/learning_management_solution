from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from courses.models import Course
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/user_registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses:course_list')
        else:
            return render(request, 'accounts/user_login.html', {'error_message': 'Invalid login credentials.'})
    return render(request, 'accounts/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def homepage(request):
    courses = Course.objects.all()
    # subscriptions = Subscription.objects.filter(user=request.user)
    # subscription_types = SubscriptionType.objects.all()
    context = {
        'courses': courses,
        # 'subscriptions': subscriptions,
        # 'subscription_types': subscription_types
    }
    return render(request, "accounts/homepage.html", context)




def dashboard(request):
    return render(request, "accounts/dashboard.html")