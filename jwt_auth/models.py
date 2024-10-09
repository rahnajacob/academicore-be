from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

SUBJECT_CHOICES = [
    ('MATHS', 'Mathematics'),
    ('PHY', 'Physics'),
    ('CHEM', 'Chemistry'),
    ('BIO', 'Biology'),
    ('ENG', 'English'),
    ('GEO', 'Geography'),
    ('HIS', 'History'),
    ('ECO', 'Economics'),
    ('COMPSCI', 'Computer Science'),
]

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default="SELECT")
    teach_fname = models.CharField(max_length=50)
    teach_lname = models.CharField(max_length=50)
    teach_dob = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.teach_fname} {self.teach_lname}'
    

#! Below: to be added in future updates, not code cemetary

# class AdminUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_staff = models.BooleanField(default=True)

# @receiver(post_save, sender=User)
# def create_teacher_profile(sender, instance, created, **kwargs):
#     if created:
#         TeacherProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_teacher_profile(sender, instance, **kwargs):
#     instance.teacherprofile.save()