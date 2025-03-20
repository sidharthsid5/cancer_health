# Create your models here.
from django.db import models


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



# Hair_Donation
class HairDonation(models.Model):
    hDonID = models.AutoField(primary_key=True)
    applydate = models.DateField()
    Guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    hairtype = models.CharField(max_length=20)
    h_image = models.CharField(max_length=20) #consider ImageField
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Hair donation {self.hDonID} by {self.Guestid}"



# Donation
class Donation(models.Model):
    donationid = models.AutoField(primary_key=True)
    Guestid = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    don_date = models.DateField()
    transactiontype = models.CharField(max_length=10)
    Cardno = models.IntegerField()
    Bank = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Donation {self.donationid} by {self.Guestid}"