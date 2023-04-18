from django.urls import path

from .views import  RegisterAPi, LoginView

urlpatterns = [
    path('register',RegisterAPi.as_view()),
    path('login',LoginView.as_view()),
]