from rest_framework import serializers
from ..models import User, TeacherProfile
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    def validate(self, data):
        password = data.pop('password') 
        password_confirmation = data.pop('password_confirmation') 
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })
        password_validation.validate_password(password=password)
        data['password'] = make_password(password)
        return data
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirmation')

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ('id', 'user', 'subject', 'teach_fname', 'teach_lname', 'teach_dob',)