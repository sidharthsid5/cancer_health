# Create your models here.
from django.db import models




# from login.models import Patient


# Cancer_type
class CancerType(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    cancertype = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.cancertype



# State
class State(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    State = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.State



# District
class Dist(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    District = models.CharField(max_length=20,null=True)
    State = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.District



# Scan_Type
class ScanType(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Scantype = models.CharField(max_length=30,null=True)
    Amount = models.IntegerField()
    Discount = models.IntegerField()

    def __str__(self):
        return self.Scantype



# Scan_Center
class ScanCenter(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Center = models.CharField(max_length=30,null=True)
    Address = models.CharField(max_length=150,null=True)
    District = models.ForeignKey(State, on_delete=models.CASCADE,null=True)  # Foreign key to District
    Phone = models.BigIntegerField()
    Mobile = models.BigIntegerField()
    Email = models.EmailField()
    Registration_date = models.DateField()

    def __str__(self):
        return self.Center



# coun_center
class CounCenter(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    counsling_center = models.CharField(max_length=30,null=True)
    Description = models.CharField(max_length=150,null=True)
    Address = models.CharField(max_length=150,null=True)
    Doctor = models.CharField(max_length=20,null=True)
    Phone = models.BigIntegerField()
    Mobile = models.BigIntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.counsling_center



# hair_don_criteria
class HairDonCriteria(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Criteria = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.Criteria



# med_services
class MedServices(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    medical_service = models.CharField(max_length=10,null=True)
    Description = models.CharField(max_length=20,null=True)
    Status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.medical_service



# GuideLines
class GuideLines(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Guides = models.CharField(max_length=10,null=True)
    added_date = models.DateField()

    def __str__(self):
        return self.Guides



# dietary_tip
class DietaryTip(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    diet_tips = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.diet_tips



# dietary_supply
class DietarySupply(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    food_group = models.CharField(max_length=10,null=True)
    daily_serving = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.food_group




# Events
class Events(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Event_title = models.CharField(max_length=10,null=True)
    Descr = models.CharField(max_length=10,null=True)
    Location = models.CharField(max_length=20,null=True)
    Event_date = models.DateField()
    event_time = models.CharField(max_length=4,null=True)

    def __str__(self):
        return self.Event_title




