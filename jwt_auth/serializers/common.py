from rest_framework import serializers
from ..models import User, TeacherProfile
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

class TeacherProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = TeacherProfile
        fields = ('id', 'user', 'subject', 'teach_fname', 'teach_lname', 'teach_dob',)

class UserSerializer(serializers.ModelSerializer):
    teacher_profile = TeacherProfileSerializer(required=False)  
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    def validate(self, data):
        password = data.pop('password') 
        password_confirmation = data.pop('password_confirmation') 
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })
        password_validation.validate_password(password=password)
        data['password'] = make_password(password)
        print('def validate thing')
        return data
    
    def create(self, validated_data):
        print('Creating user with data:', validated_data)
        teacher_profile_data = validated_data.pop('teacher_profile', None)

        user = super().create(validated_data)
        print('User created:', user)

        if validated_data.get('is_teacher') and teacher_profile_data:
            teacher_profile_data['user'] = user
            print('Creating TeacherProfile with data:', teacher_profile_data)
            TeacherProfile.objects.create(**teacher_profile_data)
    
        return user
        
        
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirmation', 'is_teacher', 'teacher_profile',)


#! Below: meant for future updates

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     request = self.context.get('request', None)
        #     if request and request.user.is_superuser:
        #         self.fields['teacher_profile'].read_only = False


    # def create(self, validated_data):
    #     print('create thing',validated_data)
    #     teacher_profile_data = validated_data.pop('teacher_profile', None)
    #     user = super().create(validated_data)
    #     if validated_data.get('is_teacher') and teacher_profile_data:
    #         teacher_profile_data['user'] = user 
    #         TeacherProfile.objects.create(**teacher_profile_data)
    #     return user