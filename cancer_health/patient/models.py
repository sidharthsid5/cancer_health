# Create your models here.
from django.db import models

from administrator.models import ScanType, ScanCenter
from login.models import Patient


class PatHealthRec(models.Model):
    Recorded = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Record_details = models.IntegerField()
    Previous_hospital = models.CharField(max_length=30,null=True)
    Treat_file = models.CharField(max_length=30,null=True)  # Consider FileField for actual files

    def __str__(self):
        return f"Record {self.Recorded} for {self.Patient}"



# Apply_Scan
class ApplyScan(models.Model):
    id = models.AutoField(primary_key=True)
    Scan_Type = models.ForeignKey(ScanType, on_delete=models.CASCADE,null=True)
    scan_center = models.ForeignKey(ScanCenter, on_delete=models.CASCADE,null=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    apply_date = models.DateField()
    booking_date = models.DateField()
    Preferred_time = models.CharField(max_length=8,null=True)
    Status = models.CharField(max_length=10,null=True)
    Apply_location = models.CharField(max_length=20,null=True)
    coupon_number = models.IntegerField()

    def __str__(self):
        return f"Scan {self.id} for {self.Patient}"



# Book_Counseling
class CounsellingBook(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Booking_date = models.DateField()
    Registration_date = models.DateField()
    Times_lot = models.IntegerField()
    Status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"Counseling {self.id} for {self.patientId}"



# Reg_FreeVig
class RegFreevig(models.Model):
    Registration_id = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Registration_date = models.DateField()
    Status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"Free Vig registration {self.Registration_id} for {self.Patient}"



# Comments
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=10,null=True)
    Date = models.DateField()
    User = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"Comment {self.id} by {self.User}"

    # Apply Scan
class ApplyScan(models.Model):
    Scan_Type = models.ForeignKey(ScanType, on_delete=models.CASCADE, null=True)
    Scan_Center = models.CharField(max_length=30, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    Booking_Date = models.DateField(null=True)
    Preferred_time = models.CharField(max_length=4, null=True)
    Status = models.CharField(max_length=6, null=True)
    Location = models.CharField(max_length=20, null=True)
    Coupon = models.CharField(max_length=6, null=True)