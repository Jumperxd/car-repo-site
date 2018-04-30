from django.db import models

from . import constants as pow_const

# Create your models here.


class PowerTrain(models.Model):
    """This model represents a vehicles powertrain"""
    model_number = models.CharField(max_length=pow_const.POWERTRAIN_MODEL_NUMBER_MAX_LENGTH)
    drivetrain = models.CharField(max_length=pow_const.POWERTRAIN_DRIVETRAIN_MAX_LENGTH)
    engine_size = models.PositiveIntegerField()

    class Meta:
        """Table Constraints"""
        unique_together = ('id', 'model_number')

    def __str__(self):
        """Convert given powertrain to a string"""
        return '{} with engine size of {}. Model Number {}.'.format(self.drivetrain,
                                                                    self.engine_size,
                                                                    self.model_number)


class VehiclePowerTrain(models.Model):
    """A model to represent the relationship between a Vehicle and PowerTrain"""
    vehicle = models.OneToOneField('vehicle.Vehicle', on_delete=models.CASCADE)
    powertrain = models.ForeignKey(PowerTrain, on_delete=models.CASCADE)

    class Meta:
        """Table constraints"""
        unique_together = ('vehicle', 'powertrain')
