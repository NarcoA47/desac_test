from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from cores.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('', include('cores.urls')),
    path('', include('subscriptions.urls')),
    path('', include('users.urls')),
    path('', include('vote.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
