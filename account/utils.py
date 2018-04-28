# Helper function for the account app.

from datetime import date


def age(born_date):
    """Calculate the age of a user based on their birth date"""
    if not born_date:
        return None
    today = date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))
