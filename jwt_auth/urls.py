from django.urls import path 
from .views import RegisterView, LoginView, UserDetailView


urlpatterns = [
    path('register/', RegisterView.as_view()), 
    path('login/', LoginView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view())
]