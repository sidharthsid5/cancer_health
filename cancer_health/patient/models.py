# Create your models here.
from django.db import models

# from cancer_health.administrator.models import ScanType, ScanCenter
# from cancer_health.registration.models import PatientReg


# Patient_healthRec
class PatHealthRec(models.Model):
    Recorded = models.AutoField(primary_key=True)
    # patientId = models.ForeignKey(PatientReg, on_delete=models.CASCADE)
    rec_det = models.IntegerField()
    prev_hospital = models.CharField(max_length=30)
    treat_file = models.CharField(max_length=30)  # Consider FileField for actual files

    def __str__(self):
        return f"Record {self.Recorded} for {self.patientId}"



# Apply_Scan
class ApplyScan(models.Model):
    Scanid = models.AutoField(primary_key=True)
    # scTypeid = models.ForeignKey(ScanType, on_delete=models.CASCADE)
    # scan_cenId = models.ForeignKey(ScanCenter, on_delete=models.CASCADE)
    # patientId = models.ForeignKey(PatientReg, on_delete=models.CASCADE)
    apply_date = models.DateField()
    booking_date = models.DateField()
    pref_time = models.CharField(max_length=8)
    Status = models.CharField(max_length=10)
    apply_loc = models.CharField(max_length=20)
    coupon_no = models.IntegerField()

    def __str__(self):
        return f"Scan {self.Scanid} for {self.patientId}"



# Book_Counseling
class CounsellingBook(models.Model):
    Counsid = models.AutoField(primary_key=True)
    # patientId = models.ForeignKey(PatientReg, on_delete=models.CASCADE)
    bookingdate = models.DateField()
    Regdate = models.DateField()
    timeslot = models.IntegerField()
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Counseling {self.Counsid} for {self.patientId}"



# Reg_FreeVig
class RegFreevig(models.Model):
    Regid = models.AutoField(primary_key=True)
    # patientId = models.ForeignKey(PatientReg, on_delete=models.CASCADE)
    Regdate = models.DateField()
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Free Vig registration {self.Regid} for {self.patientId}"



# Comments
class Comments(models.Model):
    commentsid = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=10)
    Date = models.DateField()
    User = models.CharField(max_length=10)

    def __str__(self):
        return f"Comment {self.commentsid} by {self.User}"