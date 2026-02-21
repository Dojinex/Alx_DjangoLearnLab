from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts endpoints
    path('api/accounts/', include('accounts.urls')),

    # Posts + Comments + Feed + Likes
    path('api/', include('posts.urls')),

    # Notifications
    path('api/', include('notifications.urls')),
]