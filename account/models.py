from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from . import constants as acc_const

# Create your models here.


class Profile(models.Model):
    """This model represents a User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_initial = models.CharField(max_length=acc_const.PROFILE_MIDDLE_INITIAL_MAX_LENGTH, blank=True)
    address = models.CharField(max_length=acc_const.PROFILE_ADDRESS_MAX_LENGTH, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        """Convert model to a string"""
        return self.user.username


class ProfilePhoneNumbers(models.Model):
    """This model represents User phone numbers"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    number_type = models.CharField(max_length=acc_const.PROFILE_NUMBER_TYPE_MAX_LENGTH, default=None)
    phone_number = models.CharField(max_length=acc_const.PROFILE_PHONE_NUMBER_MAX_LENGTH, default=None)

    class Meta:
        """Set table constraints"""
        unique_together = ('profile', 'phone_number')

    def __str__(self):
        """Convert phone numbers to a string."""
        return '{}: ({}) {}-{}'.format(self.number_type,
                                       self.phone_number[:3],
                                       self.phone_number[3:6],
                                       self.phone_number[-4:])


class List(models.Model):
    """This model represents a user listing a vehicle"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vehicle = models.OneToOneField('vehicle.Vehicle', on_delete=models.CASCADE)
    address = models.CharField(max_length=acc_const.LIST_ADDRESS_MAX_LENGTH)
    list_date = models.DateField(auto_now_add=True)
    car_value = models.DecimalField(max_digits=acc_const.LIST_CAR_VALUE_MAX_DIGITS,
                                    decimal_places=acc_const.LIST_CAR_VALUE_DECIMAL_PLACES)

    class Meta:
        """Constraints on this table"""
        unique_together = ('profile', 'vehicle')

    def __str__(self):
        """Convert model to a string"""
        return '{} being sold for ${} at {}. Posted by {} on {}.'.format(self.vehicle,
                                                                         self.car_value,
                                                                         self.address,
                                                                         self.profile,
                                                                         self.list_date)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    """A signal that will automatically save a Profile with a User"""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
