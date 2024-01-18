from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime as dt
from datetime import timedelta

class Userprofiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #subcription = models.ForeignKey(Subscription, related_name='user_profiles', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Userprofiles'

    def __str__(self) -> str:
        return self.user.username
