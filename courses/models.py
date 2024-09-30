from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=6)
    
    def __str__(self):
        return f'{self.code}'