# Constants for the accounts app

from _datetime import datetime

PROFILE_FIRST_NAME_MAX_LENGTH = 100
PROFILE_LAST_NAME_MAX_LENGTH = 150
PROFILE_MIDDLE_INITIAL_MAX_LENGTH = 1
PROFILE_ADDRESS_MAX_LENGTH = 200

PROFILE_PHONE_NUMBER_MAX_LENGTH = 10
PROFILE_NUMBER_TYPE_MAX_LENGTH = 30

PHONE_NUMBER_TYPE_PLACEHOLDER = 'Home, Work, Cell, etc.'
EMAIL_PLACEHOLDER = 'myemail@example.com'

LIST_SUCCESS_MESSAGE = 'Vehicle listed successfully!'
ACCOUNT_DELETION_MESSAGE = 'Deleting your account will remove all listings and you will no longer be able to log in ' \
                           'unless you create a new account.'
ALL_LIST_DELETE_MESSAGE = 'Are you sure you want to delete all listings you have?'
LIST_DELETE_MESSAGE = 'Are you sure you want to delete this listing?'

USER_CREATION_TITLE = 'Create Account'
LOGIN_TITLE = 'Log In to Account'
USER_PROFILE_TITLE = 'Your Profile Information'
LIST_VEHICLE_TITLE = 'List Address and Cost of Vehicle'
CHANGE_PASSWORD_TITLE = 'Change Password'
EDIT_ACCOUNT_TITLE = 'Edit Profile'
EDIT_LISTING_TITLE = 'Edit Listing'
CONTACT_TITLE = 'Contact Information'

PHONE_NUMBER_FORMSET_MIN_NUM = 1
PHONE_NUMBER_FORMSET_EXTRA = 0

LIST_ADDRESS_MAX_LENGTH = 200
LIST_CAR_VALUE_MAX_DIGITS = 10
LIST_CAR_VALUE_DECIMAL_PLACES = 2

NOW = datetime.now()
TODAY = '{}-{}-{}'.format(NOW.year, NOW.month, NOW.day)

MIN_DATE = '1900-01-01'
MAX_DATE = str(NOW.today().date())

STRIP_FORMAT = '%Y-%m-%d'

MIN_DATE_ERROR_MESSAGE = 'Date is too early. Minimum date input is 01/01/1900'
MIN_DATE_ERROR_CODE = 'date_minimum_preceded'
MAX_DATE_ERROR_MESSAGE = 'Date is too late. Maximum date input is today.'
MAX_DATE_ERROR_CODE = 'date_maximum_exceeded'

UNIQUE_USERNAME = 'Error: Username is already taken!'
UNIQUE_USERNAME_CODE = 'unique_username'
UNIQUE_EMAIL = 'Error: Email is already in use!'
UNIQUE_EMAIL_CODE = 'unique_email'
