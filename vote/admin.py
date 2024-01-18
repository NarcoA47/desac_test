from django.contrib import admin

from .models import Categories, Candidate, Voting

# Register your models here.
admin.site.register(Categories),
admin.site.register(Candidate),
admin.site.register(Voting)