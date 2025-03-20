# Create your models here.
from django.db import models


# Patient_Reg
class PatientReg(models.Model):
    Patientid = models.AutoField(primary_key=True)
    Patname = models.CharField(max_length=30)
    Address = models.CharField(max_length=150)
    Distid = models.IntegerField(default=1)  # Foreign key to District (later)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Photo = models.CharField(max_length=10)  # Consider using ImageField for actual images
    # cancTypeid = models.ForeignKey(CancerType, on_delete=models.CASCADE)
    DetectedDate = models.DateField()
    DetectedHospital = models.CharField(max_length=10)
    Consult_Drname = models.CharField(max_length=10)
    No_months_yr = models.IntegerField()
    Stage = models.CharField(max_length=30)
    Regdate = models.DateField()
    Status = models.CharField(max_length=30)
    Email = models.EmailField()
    Mob = models.BigIntegerField()
    Username = models.CharField(max_length=10)
    Pwd = models.CharField(max_length=4)

    def __str__(self):
        return self.Patname



# Guest
class Guest(models.Model):
    Guestid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=150)
    Distid = models.IntegerField(default=1)
    Regdate = models.DateField()
    Phone = models.BigIntegerField()
    Mob = models.IntegerField()
    Email = models.EmailField()
    Umane = models.CharField(max_length=10)
    Pwd = models.CharField(max_length=4)
    Staus = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

# Volunteer_reg
class VolunteerReg(models.Model):
    volunteerId = models.AutoField(primary_key=True)
    Guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Regdate = models.DateField()
    apply_area = models.CharField(max_length=20)
    want_loc = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Volunteer {self.volunteerId} - {self.Guestid}"