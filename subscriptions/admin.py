from django.contrib import admin
from .models import Subscribers, Subscription, UserSubscriptions, Payment, PaymentHistory

# Register your models here.
admin.site.register(Subscription),
admin.site.register(Subscribers),
admin.site.register(UserSubscriptions),
admin.site.register(Payment),
admin.site.register(PaymentHistory)