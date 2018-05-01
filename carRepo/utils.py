# Helper function for advanced searching

from account import models as acc_models

from django.contrib.auth.models import User
from django.db.models import Q

from vehicle import constants as veh_const, models as veh_models


def determine_listings(form):
    """Determine the correct context based on input parameters"""
    listings = None
    user = None
    vehicles = None
    username = form.cleaned_data['lister_username']
    address = form.cleaned_data['list_address']
    max_price = form.cleaned_data['maximum_price']
    description = form.cleaned_data['vehicle_description']
    vehicle_type = form.cleaned_data['vehicle_type']
    manufacturer = form.cleaned_data['vehicle_manufacturer']
    powertrain = form.cleaned_data['vehicle_powertrain']
    tires = form.cleaned_data['vehicle_tires']
    if username or address or max_price or description or vehicle_type or manufacturer or powertrain or tires:
        if username:
            if not User.objects.filter(username=username).exists():
                return None
            user = User.objects.get(username=username)
        if vehicle_type:
            if vehicle_type == veh_const.OTHER:
                sedans = veh_models.Sedan.objects.values_list('vehicle', flat=True)
                trucks = veh_models.Truck.objects.values_list('vehicle', flat=True)
                coupes = veh_models.Coupe.objects.values_list('vehicle', flat=True)
                suvs = veh_models.SUV.objects.values_list('vehicle', flat=True)
                vehicles = veh_models.Vehicle.objects.exclude(pk__in=sedans).exclude(pk__in=trucks).exclude(
                    pk__in=coupes).exclude(pk__in=suvs)
            else:
                if vehicle_type == veh_const.SEDAN:
                    subclass = veh_models.Sedan.objects.values_list('vehicle', flat=True)
                elif vehicle_type == veh_const.TRUCK:
                    subclass = veh_models.Truck.objects.values_list('vehicle', flat=True)
                elif vehicle_type == veh_const.COUPE:
                    subclass = veh_models.Coupe.objects.values_list('vehicle', flat=True)
                else:
                    subclass = veh_models.SUV.objects.values_list('vehicle', flat=True)
                vehicles = veh_models.Vehicle.objects.filter(pk__in=subclass)
        listings = acc_models.List.objects.all()
        if username:
            listings = listings.filter(profile=user.profile)
        if address:
            listings = listings.filter(address__icontains=address)
        if max_price:
            listings = listings.filter(car_value__lte=max_price)
        if description:
            listings = listings.filter(vehicle__description__icontains=description)
        if vehicle_type:
            listings = listings.filter(vehicle_id__in=vehicles)
        if manufacturer:
            listings = listings.filter(Q(vehicle__vehiclemanufacturer__manufacturer__name__icontains=manufacturer) |
                                       Q(vehicle__vehiclemanufacturer__manufacturer__address__icontains=manufacturer))
        if powertrain:
            listings = listings.filter(Q(vehicle__vehiclepowertrain__powertrain__model_number__icontains=powertrain) |
                                       Q(vehicle__vehiclepowertrain__powertrain__drivetrain__icontains=powertrain))
        if tires:
            listings = listings.filter(Q(vehicle__vehicletires__tires__model_number__icontains=tires) |
                                       Q(vehicle__vehicletires__tires__description__icontains=tires))
    return listings
