# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from administrator.models import Dist

from administrator.models import CancerType


# Role Model
class RoleModel(models.Model):
    Role = models.CharField(max_length=20)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Patient Registration Model
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Address = models.TextField(max_length=150)
    District = models.ForeignKey(Dist, on_delete=models.CASCADE,null=True,related_name='district')
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Photo = models.ImageField(upload_to='patient_photos/')
    Cancer_Type = models.ForeignKey(CancerType, on_delete=models.CASCADE,null=True)
    Detected_Date = models.DateField()
    Detected_Hospital = models.CharField(max_length=50)
    Consult_Doctor = models.CharField(max_length=50)
    No_months_per_year = models.IntegerField()
    Stage = models.CharField(max_length=30)
    Registration_date = models.DateField(default=django.utils.timezone.now)
    Status = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Mobile = models.BigIntegerField()
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Guest Registration Model
class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Address = models.TextField(max_length=150)
    District = models.ForeignKey(Dist, on_delete=models.CASCADE,null=True)
    Registration_date = models.DateField(default=django.utils.timezone.now)
    Phone = models.BigIntegerField()
    Mobile = models.BigIntegerField()
    Email = models.EmailField(max_length=20)
    Status = models.CharField(max_length=10)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Volunteer Registration Model
class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Registration_date = models.DateField(default=django.utils.timezone.now)
    Apply_area = models.CharField(max_length=20)
    Location = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
