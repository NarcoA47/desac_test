from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    #Login user into account on form fill
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),

    #logs out user when requested on click
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #redirects to user to dashboard after login or signup
    #check views for authentication and form contribution
    path('dashboard/', views.dashboard, name='dashboard'),

    path('zbmAmbassadors/', views.zbmAmbassadors, name='zbmAmbassadors'),
    path('kopalaAwards/', views.kopalaAwards, name='kopalaAwards'),
    path('votersChoice/', views.votersChoice, name='votersChoice'),
    path('votersGuide/', views.votersGuide, name='votersGuide'),
    path('votersView/', views.votersView, name='votersView')
]