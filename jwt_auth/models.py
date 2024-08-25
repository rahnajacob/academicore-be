from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teach_fname = models.CharField(max_length=50)
    teach_lname = models.CharField(max_length=50)
    teach_dob = models.DateField()

    def __str__(self):
        return f'{self.teach_fname} {self.teach_lname}'