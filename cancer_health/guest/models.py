# Create your models here.
from django.db import models
from login.models import Guest
from django.utils import timezone


# Hair_Donation
class HairDonation(models.Model):
    id = models.AutoField(primary_key=True)
    Apply_date = models.DateField(default=timezone.now)
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE,null=True)
    Hair_type = models.CharField(max_length=20, choices=[
        ('Straight', 'Straight'),
        ('Wavy', 'Wavy'),
        ('Curly', 'Curly'),
        ('Coily', 'Coily')
    ])
    Hair_image = models.ImageField(upload_to='hair_images/')
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"Hair donation {self.id} by {self.Guest}"



class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    Guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Donation_date = models.DateField(auto_now_add=True)
    Transaction_type = models.CharField(max_length=10, blank=True)
    Card_number = models.IntegerField(blank=True, null=True)
    Bank = models.CharField(max_length=10, blank=True)
    Status = models.CharField(max_length=10, default='Pending')
    Description = models.TextField(blank=True)
    Payment_status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f"Donation {self.id} by {self.Guest}"
