from django.urls import path
from .views import SignUpView, TeachSignUpView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('sign-up/user/', SignUpView.as_view()),
    path('sign-up/teacher/', TeachSignUpView.as_view()),
    path('sign-in/', TokenObtainPairView().as_view()),
]