from django.db import models

from . import constants as veh_const

# Create your models here.


class Vehicle(models.Model):
    """This model represents a generic vehicle"""
    description = models.CharField(max_length=veh_const.VEHICLE_TYPE_MAX_LENGTH)
    weight = models.PositiveIntegerField()

    def __str__(self):
        """Convert Vehicle model to a string"""
        return self.description


class VehicleManufacturer(models.Model):
    """This model contains relationships between manufacturers and Vehicles"""
    manufacturer = models.ForeignKey('manufacturer.Manufacturer', on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)

    class Meta:
        """Table constraints"""
        unique_together = ('manufacturer', 'vehicle')


class Sedan(models.Model):
    """This model represents a Sedan vehicle"""
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    sedan_class = models.CharField(max_length=veh_const.SEDAN_CLASS_MAX_LENGTH)

    def __str__(self):
        """Convert Sedan to a string"""
        return '{} with sedan class of {}.'.format(self.vehicle, self.sedan_class)


class Truck(models.Model):
    """This model represents a Truck vehicle"""
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    truck_bed_length = models.DecimalField(max_digits=veh_const.TRUCK_BED_LENGTH_MAX_DIGITS,
                                           decimal_places=veh_const.TRUCK_BED_LENGTH_DECIMAL_PLACES)
    truck_bed_width = models.DecimalField(max_digits=veh_const.TRUCK_BED_WIDTH_MAX_DIGITS,
                                          decimal_places=veh_const.TRUCK_BED_WIDTH_DECIMAL_PLACES)

    def __str__(self):
        """Convert Truck to a string"""
        return '{} with a bed length of {} and width of {}.'.format(self.vehicle,
                                                                    self.truck_bed_length,
                                                                    self.truck_bed_width)


class Coupe(models.Model):
    """This model represents a Coupe vehicle"""
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    top_style = models.CharField(max_length=veh_const.COUPE_TOP_STYLE_MAX_LENGTH)

    def __str__(self):
        """Convert Coupe to a string"""
        return '{} with a top style of {}.'.format(self.vehicle, self.top_style)


class SUV(models.Model):
    """This model represents an SUV vehicle"""
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    towing_capacity = models.PositiveIntegerField()

    def __str__(self):
        """Convert SUV to a string"""
        return '{} with a towing capacity of {}.'.format(self.vehicle, self.towing_capacity)
