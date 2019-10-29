from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Packages(models.Model):

    class Meta:
        verbose_name_plural = "Packages"

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

    class Meta:
        verbose_name_plural = "Destination details"

    place_id = models.CharField(max_length=25, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)
    visiting_on = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    place_image = models.ImageField(upload_to='places')


class PackagesGuide(models.Model):

    class Meta:
        verbose_name_plural = "Package guide"

    guide_id = models.CharField(max_length=25, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='guides', default="../static/travello/images/main2.jpg")
    guide_name = models.CharField(max_length=20)
    age = models.IntegerField()
    experience = models.IntegerField()


class PackagesVehicle(models.Model):

    class Meta:
        verbose_name_plural = "Package vehicles"

    reg_number = models.CharField(max_length=13, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    vehicle_image_1 = models.ImageField(upload_to='vehicles', default=None)
    vehicle_image_2 = models.ImageField(upload_to='vehicles', default=None)
    vehicle_image_3 = models.ImageField(upload_to='vehicles', default=None)
    vehicle_image_4 = models.ImageField(upload_to='vehicles', default=None)


class PackagesHotel(models.Model):

    class Meta:
        verbose_name_plural = "Package hotels"

    hotel_id = models.CharField(max_length=35, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=20)
    room_capacity = models.IntegerField()
    hotel_image_1 = models.ImageField(upload_to='hotels', default=None)
    hotel_image_2 = models.ImageField(upload_to='hotels', default=None)
    hotel_image_3 = models.ImageField(upload_to='hotels', default=None)
    hotel_image_4 = models.ImageField(upload_to='hotels', default=None)
    hotel_image_5 = models.ImageField(upload_to='hotels', default=None)
    hotel_image_6 = models.ImageField(upload_to='hotels', default=None)


class PackagesBookings(models.Model):

    class Meta:
        verbose_name_plural = "Booking details"

    booking_id = models.CharField(max_length=150, primary_key=True)
    location_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    username = models.ForeignKey(User, max_length=150, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_amount = models.IntegerField()
