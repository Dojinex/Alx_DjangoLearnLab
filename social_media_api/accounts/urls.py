from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from django.urls import path, include


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
]



urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
]
