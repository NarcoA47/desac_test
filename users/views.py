from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from subscriptions.models import Subscription,Subscribers,UserSubscriptions
from vote.vote import Vote
from vote.models import Candidate, Categories
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required  
def dashboard(request):

    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:9]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)

    return render (request, 'pages/account.html', {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })
#@login_required  
def zbmAmbassadors(request):
    
    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:4]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)
    
    return render (request, 'pages/voters-page-1.html', {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })

#@login_required  
def kopalaAwards(request):
    
    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:1]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)
    
    return render(request, 'pages/voters-page-2.html' , {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })

#@login_required  
def votersChoice(request):
    
    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:1]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)
    
    return render (request, 'pages/voters-choice.html' , {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })

#@login_required  
def votersGuide(request):
    
    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:1]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)
    
    return render (request, 'pages/voters-guide.html' , {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })

#@login_required  
def votersView(request):
    
    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() 
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)
    
    return render (request, 'pages/voters-view.html' , {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })