# Helper function for advanced searching

from account import models as acc_models

from django.contrib.auth.models import User

from vehicle import constants as veh_const, models as veh_models


def determine_listings(form):
    """Determine the correct context based on input parameters"""
    listings = None
    user = None
    vehicles = None
    username = form.cleaned_data['username']
    address = form.cleaned_data['address']
    max_price = form.cleaned_data['max_price']
    vehicle_type = form.cleaned_data['vehicle_type']
    if username or address or max_price or vehicle_type:
        if username:
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
        if username and address and max_price and vehicle_type:
            listings = acc_models.List.objects.filter(profile=user.profile,
                                                      vehicle_id__in=vehicles,
                                                      address__contains=address,
                                                      car_value__lte=max_price)
        elif username and address and max_price:
            listings = acc_models.List.objects.filter(profile=user.profile,
                                                      address__contains=address,
                                                      car_value__lte=max_price)
        elif username and address and vehicle_type:
            listings = acc_models.List.objects.filter(profile=user.profile,
                                                      address__contains=address,
                                                      vehicle_id__in=vehicles)
        elif username and max_price and vehicle_type:
            listings = acc_models.List.objects.filter(profile=user.profile,
                                                      car_value__lte=max_price,
                                                      vehicle_id__in=vehicles)
        elif address and max_price and vehicle_type:
            listings = acc_models.List.objects.filter(address__contains=address,
                                                      car_value__lte=max_price,
                                                      vehicle_id__in=vehicles)
        elif username and address:
            listings = acc_models.List.objects.filter(profile=user.profile, address__contains=address)
        elif username and max_price:
            listings = acc_models.List.objects.filter(profile=user.profile, car_value__lte=max_price)
        elif username and vehicle_type:
            listings = acc_models.List.objects.filter(profile=user.profile, vehicle_id__in=vehicles)
        elif address and max_price:
            listings = acc_models.List.objects.filter(address__contains=address, car_value__lte=max_price)
        elif address and vehicle_type:
            listings = acc_models.List.objects.filter(address__contains=address, vehicle_id__in=vehicles)
        elif max_price and vehicle_type:
            listings = acc_models.List.objects.filter(car_value__lte=max_price, vehicle_id__in=vehicles)
        elif username:
            listings = acc_models.List.objects.filter(profile=user.profile)
        elif address:
            listings = acc_models.List.objects.filter(address__contains=address)
        elif max_price:
            listings = acc_models.List.objects.filter(car_value__lte=max_price)
        else:
            listings = acc_models.List.objects.filter(vehicle_id__in=vehicles)
    return listings
