# Helper functions for the vehicle app

from vehicle import constants as veh_const, models as veh_models


def delete_associated_subclass(listing):
    """Delete previously associated subclass of vehicle before changing it"""
    if veh_models.Sedan.objects.filter(vehicle=listing.vehicle).exists():
        veh_models.Sedan.objects.filter(vehicle=listing.vehicle).delete()
    elif veh_models.Truck.objects.filter(vehicle=listing.vehicle).exists():
        veh_models.Truck.objects.filter(vehicle=listing.vehicle).delete()
    elif veh_models.Coupe.objects.filter(vehicle=listing.vehicle):
        veh_models.Coupe.objects.filter(vehicle=listing.vehicle).delete()
    elif veh_models.SUV.objects.filter(vehicle=listing.vehicle).exists():
        veh_models.SUV.objects.filter(vehicle=listing.vehicle).delete()