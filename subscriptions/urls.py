from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    #redirects to the subscription page if not subscribed
    path('subscription/', views.subscription, name='subscription'),

    #path('onboardingOne/', views.onboardingOne, name='onboardingOne'),

    path('onboardingTwo/', views.onboardingTwo, name='onboardingTwo'),

    #redirects to the vote renew page and lets you purchase more votes
    path('renew/', views.renew, name='renew'), 

    #Checks for user subscription and confirms if your subscribed or not, it als ends the subscription
    path('endsub/', views.endsub, name='endsub'),
]