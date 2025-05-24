# Create your models here.
import django.utils.timezone
from django.db import models

from administrator.models import ScanType, ScanCenter
from login.models import Patient

# Patient Health Records
class PatHealthRec(models.Model):
    Recorded = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Records_Details = models.CharField(max_length=30,null=True)
    Previous_hospital = models.CharField(max_length=30,null=True)
    Treat_file = models.FileField(upload_to='patient_photos/', null=True, blank=True)

    def __str__(self):
        return f"Record {self.Recorded} for {self.Patient}"


# Book_Counseling
class CounsellingBook(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Booking_date = models.DateField()
    Registration_date = models.DateField(default=django.utils.timezone.now)
    Times_lot = models.CharField(max_length=20, null=True)
    Status = models.CharField(default='Pending',max_length=10,null=True)
    Coupon = models.CharField(max_length=6, null=True)

    def __str__(self):
        return f"Counseling {self.id} for {self.patientId}"



# Reg_FreeVig
class RegFreevig(models.Model):
    Registration_id = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Registration_date = models.DateField(default=django.utils.timezone.now)
    Status = models.CharField(default= 'Pending',max_length=10,null=True)
    Full_Name = models.CharField(max_length=100,null=True)
    Age = models.PositiveIntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],null=True)
    Phone = models.CharField(max_length=15,null=True)
    Address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Free Vig registration {self.Registration_id} for {self.Patient}"



# Comments
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=100,null=True)
    Date = models.DateField(default=django.utils.timezone.now)
    Patient =models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Comment {self.id} by {self.Patient}"

    # Apply Scan
class ApplyScan(models.Model):
    Scan_Type = models.ManyToManyField(ScanType)
    Scan_Center = models.ForeignKey(ScanCenter, on_delete=models.CASCADE,null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    Booking_Date = models.DateField(null=True)
    Preferred_time = models.CharField(max_length=20, null=True)
    Status = models.CharField(default='New', max_length=20)
    Amount = models.IntegerField(null=True)
    Coupon = models.CharField(max_length=6, null=True)

