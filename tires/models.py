from django.db import models

from . import constants as tire_const

# Create your models here.


class Tires(models.Model):
    """This model will represent tires on a vehicle"""
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE, default=None)
    model_number = models.CharField(max_length=tire_const.TIRES_MODEL_NUMBER_MAX_LENGTH, default=None)
    description = models.CharField(max_length=tire_const.TIRES_DESCRIPTION_MAX_LENGTH, default=None)

    class Meta:
        """Define constraints on Tires table"""
        unique_together = ('vehicle', 'model_number')

    def __str__(self):
        """Convert Tires to a string"""
        return self.description
