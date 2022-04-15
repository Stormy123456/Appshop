from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_foods.models import Food
from .models import Subscription
from app_general.forms import SubscriptionModelForm

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subscription_thankyou'))
    else:    
        form = SubscriptionModelForm()
    context = {'form':form}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')