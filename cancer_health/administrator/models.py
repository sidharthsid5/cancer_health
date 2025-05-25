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
    Scan_Type = models.CharField(max_length=30,null=True)
    Amount = models.IntegerField()
    Discount = models.IntegerField()

    def __str__(self):
        return self.Scan_Type



# Scan_Center
class ScanCenter(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Center = models.CharField(max_length=30,null=True)
    Address = models.CharField(max_length=150,null=True)
    District = models.ForeignKey(Dist, on_delete=models.CASCADE,null=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField()
    Registration_date = models.DateField()

    def __str__(self):
        return self.Center



# coun_center
class CounCenter(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    counsling_center = models.CharField(max_length=50,null=True)
    Description = models.CharField(max_length=350,null=True)
    Address = models.CharField(max_length=250,null=True)
    Doctor = models.CharField(max_length=100,null=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField()

    def __str__(self):
        return self.counsling_center



# hair_don_criteria
class HairDonCriteria(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Criteria = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.Criteria



# med_services
class MedServices(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    medical_service = models.CharField(max_length=50,null=True)
    Description = models.CharField(max_length=200,null=True)
    Status = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.medical_service



# GuideLines
class GuideLines(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Guides = models.CharField(max_length=200,null=True)
    added_date = models.DateField()

    def __str__(self):
        return self.Guides


# dietary_tip
class DietaryTip(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    diet_tips = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.diet_tips


# dietary_supply
class DietarySupply(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    food_group = models.CharField(max_length=100,null=True)
    daily_serving = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.food_group


# Events
class Events(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    Event_title = models.CharField(max_length=20,null=True)
    Description = models.CharField(max_length=300,null=True)
    Location = models.CharField(max_length=20,null=True)
    Event_date = models.DateField()
    event_time = models.CharField(max_length=8,null=True)

    def __str__(self):
        return self.Event_title




