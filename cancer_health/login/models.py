

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# Role Model
class RoleModel(models.Model):
    Role = models.CharField(max_length=20)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Patient Registration Model
class Patient(models.Model):
    Patientid = models.AutoField(primary_key=True)
    Patname = models.CharField(max_length=30)
    Address = models.TextField(max_length=150)
    Distid = models.IntegerField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Photo = models.ImageField(upload_to='patient_photos/')
    cancTypeid = models.IntegerField()
    DetectedDate = models.DateField()
    DetectedHospital = models.CharField(max_length=50)
    Consult_Drname = models.CharField(max_length=50)
    No_months_yr = models.IntegerField()
    Stage = models.CharField(max_length=30)
    Regdate = models.DateField(default=django.utils.timezone.now)
    Status = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Mob = models.BigIntegerField()
    Username = models.CharField(max_length=10, unique=True)
    Pwd = models.CharField(max_length=10)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Guest Registration Model
class Guest(models.Model):
    Guestid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Address = models.TextField(max_length=150)
    Distid = models.IntegerField()
    Regdate = models.DateField(default=django.utils.timezone.now)
    Phone = models.BigIntegerField()
    Mob = models.BigIntegerField()
    Email = models.EmailField(max_length=20)
    Uname = models.CharField(max_length=10, unique=True)
    Pwd = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Volunteer Registration Model
class Volunteer(models.Model):
    volunteerId = models.AutoField(primary_key=True)
    Guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Regdate = models.DateField(default=django.utils.timezone.now)
    apply_area = models.CharField(max_length=20)
    want_loc = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
