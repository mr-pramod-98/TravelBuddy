from django.contrib import admin
from .models import Packages, PackagesBookings, PackagesGuide, PackagesHotel, PackagesVehicle, DestinationDetails

# Register your models here.
admin.site.register(Packages)
admin.site.register(PackagesVehicle)
admin.site.register(PackagesHotel)
admin.site.register(PackagesGuide)
admin.site.register(PackagesBookings)
admin.site.register(DestinationDetails)
