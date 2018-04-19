from django.db import models
from django.contrib.auth.models import User

from . import constants as acc_const

# Create your models here.


class Profile(models.Model):
    """This model represents a User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_initial = models.CharField(max_length=acc_const.PROFILE_MIDDLE_INITIAL_MAX_LENGTH, blank=True)
    address = models.CharField(max_length=acc_const.PROFILE_ADDRESS_MAX_LENGTH, blank=True)
    date_of_birth = models.DateField()


class ProfilePhoneNumbers(models.Model):
    """This model represents User phone numbers"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=acc_const.PROFILE_PHONE_NUMBER_MAX_LENGTH)

    class Meta:
        """Set table constraints"""
        unique_together = ('profile', 'phone_number')

    def __str__(self):
        """Convert phone numbers to a string."""
        return '({}) {}-{}'.format(self.phone_number[:3], self.phone_number[3:6], self.phone_number[-4:])
