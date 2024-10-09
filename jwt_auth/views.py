from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TeacherProfile, User
from .serializers.common import UserSerializer, TeacherProfileSerializer
from django.contrib.auth import get_user_model
from utils.decorators import handle_exceptions
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# Create your views here.
class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        user_to_create=UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user = user_to_create.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message':'User successful sign up',
                'access': str(refresh.access_token),
                'refresh': str(refresh)})
        return Response(user_to_create.errors)

#! below here is edited stuff

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework import status


class TeachSignUpView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        is_teacher = request.data.get('is_teacher', False)
        is_staff = request.data.get('is_staff', False)
        teach_fname = request.data.get('teach_fname')
        teach_lname = request.data.get('teach_lname')

        # Check if password and confirmation match
        if password != password_confirmation:
            return JsonResponse({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create the user
            user = User.objects.create(
                username=username,
                password=make_password(password),  
                is_teacher=is_teacher,
                is_staff=is_staff
            )
            # Create the TeacherProfile
            TeacherProfile.objects.create(
                user=user,
                teach_fname=teach_fname,
                teach_lname=teach_lname
            )

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            print("Access Token:", access_token)
            print("Refresh Token:", refresh_token)

        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({
            'message': 'Teacher profile created successfully',
            'access': access_token,  
            'refresh': refresh_token}, status=status.HTTP_201_CREATED)

    
# class TeachSignUpView(APIView):
#     @handle_exceptions
#     def post(self, request):
#         teach_to_create=TeacherProfileSerializer(data=request.data)
#         if teach_to_create.is_valid():
#             teach_to_create.save()
#             return Response('Teach successful sign up')
#         return Response(teach_to_create.errors)