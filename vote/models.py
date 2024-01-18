from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime as dt
from datetime import timedelta
from users.models import User
from subscriptions.models import Subscribers, Subscription, UserSubscriptions

class Categories(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

# Create your models here.
class Candidate(models.Model):
    category = models.ForeignKey(Categories, related_name='modals', on_delete=models.CASCADE)
    modal_name = models.CharField(max_length=300)
    modal_slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='templates/uploads/', blank=True, null=True)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Candidate'

    def __str__(self) -> str:
        return self.modal_name
    

#This is the applicaion that lets users vote
class Voting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    voted = models.IntegerField(default=0)