# Models for a manufacturer

from carRepo import validators as main_val

from django.db import models

from . import constants as man_const

# Create your models here.


class Manufacturer(models.Model):
    """This model represent a manufacturer of a vehicle."""
    name = models.CharField(max_length=man_const.MANUFACTURER_NAME_MAX_LENGTH, validators=[main_val.validate_strings])
    address = models.CharField(max_length=man_const.MANUFACTURER_ADDRESS_MAX_LENGTH)

    def __str__(self):
        """This function will translate this model to a string"""
        return self.name


class ManufacturerPhoneNumbers(models.Model):
    """This class will contain the multi attribute phone number"""
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    number_type = models.CharField(max_length=man_const.MANUFACTURER_PHONE_TYPE_MAX_LENGTH,
                                   default=None,
                                   validators=[main_val.validate_strings])
    phone_number = models.CharField(max_length=man_const.MANUFACTURER_PHONE_MAX_LENGTH,
                                    default=None,
                                    validators=[main_val.validate_phone_number])

    class Meta:
        """Specify constraints for this table"""
        unique_together = ('manufacturer', 'phone_number')

    def __str__(self):
        """This function will translate this model to a string"""
        return '{}: ({}) {}-{}'.format(self.number_type,
                                       self.phone_number[:3],
                                       self.phone_number[3:6],
                                       self.phone_number[-4:])
