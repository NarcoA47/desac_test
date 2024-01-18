from django.shortcuts import render, redirect
from users.models import Userprofiles
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from users.models import Userprofiles 
from .models import Subscribers, Subscription, UserSubscriptions

#def onboardingOne(request):
#    if request.method == 'POST':
#        email = request.POST['email']
#
#        if User.objects.filter(email=email).exists():  
#           messages.error(request, "Email already exists!! Please try another username")
#            return redirect('onboardingOne')
#
#        messages.success(request, "Your Account has been successfully created.")
#        return redirect('onboardingTwo')
#    
#    return render(request, "pages/page-1.html")

def onboardingTwo(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():  
            messages.error(request, "Email already exists!! Please try another username")
            return redirect('onboardingTwo')
        
        if User.objects.filter(email=email).exists():  
           messages.error(request, "Email already exists!! Please try another username")
           return redirect('onboardingOne')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
        
        if password != confirm_password:
            messages.error(request, "Password does not match! ")
        
        user = User.objects.create_user(username, email, password)
        user.save()

        userprofile = Userprofiles.objects.create(user=user)
        
        #connect the subscription to the user registration form
        get_subscription = Subscription.objects.get(subscription_type='Free')
        UserSubscriptions.objects.create(user=user, subscription=get_subscription)
        messages.success(request, "Registration successful." )


        messages.success(request, "Your Account has been successfully created.")
        return redirect('dashboard')
    
    return render(request, "pages/page-2.html")

def subscription(request):
    plan = request.GET.get('sub_plan')
    fetch_subscription = Subscription.objects.filter(subscription_type=plan).exists()
    if fetch_subscription == False:
        return redirect('subscription')
    subscription = Subscription.objects.get(subscription_type=plan)
    #print(subscription)
    return render (request, 'pages/subscription.html')

#Renew subscription, for the votes
def renew(request):
    return render (request, 'pages/add-votes.html')

#checks for user subscription
def endsub(request):
    return render (request, 'pages/end-sub')