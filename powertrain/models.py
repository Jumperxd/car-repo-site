from django.db import models

from . import constants as pow_const

# Create your models here.


class PowerTrain(models.Model):
    """This model represents a vehicles powertrain"""
    vehicle = models.ForeignKey('vehicle.Vehicle', on_delete=models.CASCADE)
    model_number = models.CharField(max_length=pow_const.POWERTRAIN_MODEL_NUMBER_MAX_LENGTH)
    drivetrain = models.CharField(max_length=pow_const.POWERTRAIN_DRIVETRAIN_MAX_LENGTH)
    engine_size = models.PositiveIntegerField()

    class Meta:
        """Define constraints for a powertrain"""
        unique_together = ('vehicle', 'model_number')

    def __str__(self):
        """Convert given powertrain to a string"""
        return '{} with engine size of {}'.format(self.drivetrain, self.engine_size)
