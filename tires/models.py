from django.db import models

from . import constants as tire_const

# Create your models here.


class Tires(models.Model):
    """This model will represent tires on a vehicle"""
    model_number = models.CharField(max_length=tire_const.TIRES_MODEL_NUMBER_MAX_LENGTH, default=None)
    description = models.CharField(max_length=tire_const.TIRES_DESCRIPTION_MAX_LENGTH, default=None)

    class Meta:
        """Table constraints"""
        unique_together = ('id', 'model_number')

    def __str__(self):
        """Convert Tires to a string"""
        return '{}. Model Number {}.'.format(self.description, self.model_number)


class VehicleTires(models.Model):
    """This model represents the relationship between a Vehicle and Tires"""
    vehicle = models.OneToOneField('vehicle.Vehicle', on_delete=models.CASCADE)
    tires = models.ForeignKey(Tires, on_delete=models.CASCADE)

    class Meta:
        """Table constraints"""
        unique_together = ('vehicle', 'tires')
