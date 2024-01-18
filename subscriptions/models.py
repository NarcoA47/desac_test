from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime as dt
from datetime import timedelta
from users.models import User

# Create your models here.
#Subscription for the voters payment plans
#Creates a subscription process in the database about user
#Provides subscription plans for user
#Identifies all user subscription data management
class Subscription(models.Model):
    SUBSCRIPTION_CHOICES = (
        ('Premium', 'Premium'),
        ('PremiumPlus', 'PremiumPlus'),
        ('Free', 'Free')
    )

    SUBSCRIPTION_DURATION = (
        ('Three_Days', 'Three_Days'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )

    NUMBER_OF_VOTES = {
        ('3', '3'),
        ('5', '5'),
        ('8','8'),
    }

    slug = models.SlugField(null=True, blank=True)
    subscription_type = models.CharField(choices=SUBSCRIPTION_CHOICES, default='Free', max_length=30)
    number_of_votes = models.CharField(choices=NUMBER_OF_VOTES, default='Free', max_length=30)
    duration = models.PositiveIntegerField(default=3)
    duration_period = models.CharField(max_length=100, default='Free ', choices=SUBSCRIPTION_DURATION, )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Subscription'

    def __str__(self) -> str:
        return self.subscription_type
    

class Payment(models.Model):
    user_profiles = models.ForeignKey(User, related_name='payment', on_delete=models.CASCADE)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.user_profiles

#Payment History
#Shows the payment history of the user from the database
class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    payment_for = models.ForeignKey('Subscription', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'PaymentHistory'

    def __str__(self) -> str:
        return self.user.username  
    

class UserSubscriptions(models.Model):
    user = models.OneToOneField(User, related_name='user_subscription', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, related_name='user_subscription', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'UserSubscriptions'

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=UserSubscriptions)
def create_subscription(sender, instance, *args, **kwargs):
    if instance:
        Subscribers.objects.create(user_subscription=instance, expires_in=dt.datetime.now().date() + timedelta(days=instance.subscription.duration))

#This model shows all users that have created and account and have subscribed to the platform
class Subscribers(models.Model):
    user_subscription = models.ForeignKey(UserSubscriptions, related_name='subscribers', on_delete=models.CASCADE, default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.user_subscription.user.username