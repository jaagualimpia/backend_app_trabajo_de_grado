from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis_result = models.CharField(max_length=100)
    diagnosis_date = models.DateTimeField(auto_now_add=True)
    patient_date_of_birth = models.DateTimeField(auto_now=False)
    patient_name = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='images/', blank=True, null=True)


    