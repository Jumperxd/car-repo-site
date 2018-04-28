# Validators for account app

import time

from django.core.exceptions import ValidationError

from . import constants as acc_const


def validate_birth_date(birth_date):
    """A validator for a birth date"""
    if birth_date != '':
        date_comp = time.strptime(str(birth_date), acc_const.STRIP_FORMAT)
        min_date = time.strptime(acc_const.MIN_DATE, acc_const.STRIP_FORMAT)
        max_date = time.strptime(acc_const.MAX_DATE, acc_const.STRIP_FORMAT)
        if date_comp < min_date:
            raise ValidationError(acc_const.MIN_DATE_ERROR_MESSAGE, acc_const.MIN_DATE_ERROR_CODE)
        elif date_comp > max_date:
            raise ValidationError(acc_const.MAX_DATE_ERROR_MESSAGE, acc_const.MAX_DATE_ERROR_CODE)
