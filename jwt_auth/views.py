from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, TeacherProfile
from .serializers.common import UserSerializer

# Create your views here.
class SignUpView(APIView):
    def post(self, request):
        return Response('HIT SIGN UP')