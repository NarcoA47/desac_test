from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    #add votes to the voted button when the user adds clicks vote
    path('vote/int:vote_id/', views.vote, name='vote'),

    #Create vote for every user who clicks the votes
    path('createvote/str:vote_id/', views.createvote, name='createvote'),

    #create a path for the categories in the homepage
    path('<slug:slug>/', views.category_details, name="category_details"),
]