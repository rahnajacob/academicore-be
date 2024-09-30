from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TeacherProfile
from .serializers.common import UserSerializer, TeacherProfileSerializer
from django.contrib.auth import get_user_model
from utils.decorators import handle_exceptions

User = get_user_model()

# Create your views here.
class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        user_to_create=UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response('User successful sign up')
        return Response(user_to_create.errors)
    
class TeachSignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        teach_to_create=TeacherProfileSerializer(data=request.data)
        if teach_to_create.is_valid():
            teach_to_create.save()
            return Response('Teach successful sign up')
        return Response(teach_to_create.errors)