# Create your models here.
from django.db import models
from login.models import Guest

# # Hair_Donation
class HairDonation(models.Model):
    id = models.AutoField(primary_key=True)
    Apply_date = models.DateField()
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Hair_type = models.CharField(max_length=20)
    Hair_image = models.CharField(max_length=20) #consider ImageField
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Hair donation {self.id} by {self.Guest}"



# Donation
class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Donation_date = models.DateField()
    Transaction_type = models.CharField(max_length=10)
    Card_number = models.IntegerField()
    Bank = models.CharField(max_length=10)
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Donation {self.id} by {self.Guest}"