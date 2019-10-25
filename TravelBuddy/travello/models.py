from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Packages(models.Model):
    location_id = models.CharField(max_length=15, primary_key=True)
    location_name = models.CharField(max_length=50)
    sub_title = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    days = models.IntegerField()
    date = models.DateField()
    total_number_seats = models.IntegerField()
    destination_image = models.ImageField(upload_to='destinations')


class DestinationDetails(models.Model):
    place_id = models.CharField(max_length=25, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)
    visiting_on = models.IntegerField(default=0)
    place_image = models.ImageField(upload_to='places')


class PackagesGuide(models.Model):
    guide_id = models.CharField(max_length=25, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=20)
    age = models.IntegerField()
    experience = models.IntegerField()


class PackagesVehicle(models.Model):
    reg_number = models.CharField(max_length=13, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    capacity = models.IntegerField()


class PackagesHotel(models.Model):
    hotel_id = models.CharField(max_length=35, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=20)
    room_capacity = models.IntegerField()


class PackagesBookings(models.Model):
    booking_id = models.CharField(max_length=150, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    username = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_amount = models.IntegerField()
