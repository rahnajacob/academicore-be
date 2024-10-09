from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='courses_created'
    )
    
    def __str__(self):
        return f'{self.code}'