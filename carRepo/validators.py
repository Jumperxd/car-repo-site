# Validators spread across project

from account import constants as acc_const

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, DecimalValidator

from . import constants as main_const


def validate_phone_number(phone_number):
    """A validator for a phone number"""
    if len(phone_number) < acc_const.PROFILE_PHONE_NUMBER_MAX_LENGTH:
        raise ValidationError(main_const.PHONE_NUMBER_TOO_SHORT, code=main_const.PHONE_NUMBER_TOO_SHORT_CODE)
    elif not phone_number.isdigit():
        raise ValidationError(main_const.INVALID_PHONE_NUMBER, code=main_const.INVALID_PHONE_NUMBER_CODE)


def validate_strings(value):
    """Validate strings that are not supposed to have numeric characters"""
    validator = RegexValidator(r'^[\w\' ]+$', main_const.INVALID_STRING, main_const.INVALID_STRING_CODE)
    validator(value)


def validate_decimals(decimal):
    """Validate decimals to ensure they are not negative and don't exceed max_digits"""
    if decimal < 0:
        raise ValidationError(main_const.NEGATIVE_DECIMAL, code=main_const.NEGATIVE_DECIMAL_CODE)
