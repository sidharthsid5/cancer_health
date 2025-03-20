# Create your models here.
from django.db import models


#Admin
class Admin(models.Model):
    u_name = models.CharField(max_length=10, primary_key=True)
    Pwd = models.CharField(max_length=10)

    def __str__(self):
        return self.u_name



# Cancer_type
class CancerType(models.Model):
    cancTypeid = models.AutoField(primary_key=True)
    cancertype = models.CharField(max_length=30)

    def __str__(self):
        return self.cancertype



# State
class State(models.Model):
    Stateid = models.AutoField(primary_key=True)
    State = models.CharField(max_length=20)

    def __str__(self):
        return self.State



# District
class Dist(models.Model):
    Distid = models.AutoField(primary_key=True)
    Dist = models.CharField(max_length=20)
    Stateid = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.Dist



# Scan_Type
class ScanType(models.Model):
    scTypeid = models.AutoField(primary_key=True)
    Scantype = models.CharField(max_length=30)
    Amount = models.IntegerField()
    Discount = models.IntegerField()

    def __str__(self):
        return self.Scantype



# Scan_Center
class ScanCenter(models.Model):
    scan_cenid = models.AutoField(primary_key=True)
    Center = models.CharField(max_length=30)
    Address = models.CharField(max_length=150)
    Distid = models.IntegerField(default=1)  # Foreign key to District
    Phone = models.BigIntegerField()
    Mob = models.BigIntegerField()
    Email = models.EmailField()
    Regdate = models.DateField()

    def __str__(self):
        return self.Center



# coun_center
class CounCenter(models.Model):
    coun_centreid = models.AutoField(primary_key=True)
    coun_center = models.CharField(max_length=30)
    Descr = models.CharField(max_length=150)
    Address = models.CharField(max_length=150)
    Doctor = models.CharField(max_length=20)
    Phone = models.BigIntegerField()
    Mob = models.BigIntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.coun_center



# hair_don_criteria
class HairDonCriteria(models.Model):
    criteriaid = models.AutoField(primary_key=True)
    Criteria = models.CharField(max_length=30)

    def __str__(self):
        return self.Criteria



# med_services
class MedServices(models.Model):
    mserv_id = models.AutoField(primary_key=True)
    med_service = models.CharField(max_length=10)
    Descr = models.CharField(max_length=20)
    Status = models.CharField(max_length=10)

    def __str__(self):
        return self.med_service



# GuideLines
class GuideLines(models.Model):
    guId = models.AutoField(primary_key=True)
    Guides = models.CharField(max_length=10)
    added_date = models.DateField()

    def __str__(self):
        return self.Guides



# dietary_tip
class DietaryTip(models.Model):
    Dietid = models.AutoField(primary_key=True)
    diet_tips = models.CharField(max_length=10)

    def __str__(self):
        return self.diet_tips



# dietary_supply
class DietarySupply(models.Model):
    diet_supplyid = models.AutoField(primary_key=True)
    food_gp = models.CharField(max_length=10)
    sugg_daily_serv = models.CharField(max_length=20)

    def __str__(self):
        return self.food_gp




# Events
class Events(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventTitle = models.CharField(max_length=10)
    Descr = models.CharField(max_length=10)
    Location = models.CharField(max_length=20)
    eventdate = models.DateField()
    ev_time = models.CharField(max_length=4)

    def __str__(self):
        return self.eventTitle