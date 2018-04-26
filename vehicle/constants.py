# Constants for Vehicle app

VEHICLE_TYPE_MAX_LENGTH = 100

SEDAN_CLASS_MAX_LENGTH = 50

TRUCK_BED_LENGTH_MAX_DIGITS = 6
TRUCK_BED_LENGTH_DECIMAL_PLACES = 2
TRUCK_BED_WIDTH_MAX_DIGITS = 6
TRUCK_BED_WIDTH_DECIMAL_PLACES = 2

COUPE_TOP_STYLE_MAX_LENGTH = 100

VEHICLE_TYPE_PLACEHOLDER = 'Sedan, SUV, Toyota, 4-Door, Red, etc.'
VEHICLE_WEIGHT_PLACEHOLDER = 'lbs.'
TRUCK_BED_LENGTH_AND_WIDTH_PLACEHOLDER = 'inches'
SUV_TOWING_CAPACITY_PLACEHOLDER = 'lbs.'

ADD_VEHICLE_TITLE = 'Add A New Vehicle'
ADD_SEDAN_TITLE = 'Add A New Sedan'
ADD_TRUCK_TITLE = 'Add A New Truck'
ADD_COUPE_TITLE = 'Add A New Coupe'
ADD_SUV_TITLE = 'Add A New SUV'

INAPPLICABLE = ''
SEDAN = '2'
TRUCK = '3'
COUPE = '4'
SUV = '5'
OTHER = '6'
VEHICLE_TYPE_CHOICES = ((INAPPLICABLE, '------------'),
                        (SEDAN, 'Sedan'),
                        (TRUCK, 'Truck'),
                        (COUPE, 'Coupe'),
                        (SUV, 'SUV'),
                        (OTHER, 'Other'))
