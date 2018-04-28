# Helper functions for the vehicle app

from vehicle import constants as veh_const, models as veh_models


def delete_associated_subclass(listing, vehicle_type):
    """Delete previously associated subclass of vehicle before changing it"""
    if vehicle_type == veh_const.SEDAN:
        veh_models.Sedan.objects.filter(vehicle=listing.vehicle).delete()
    elif vehicle_type == veh_const.TRUCK:
        veh_models.Truck.objects.filter(vehicle=listing.vehicle).delete()
    elif vehicle_type == veh_const.COUPE:
        veh_models.Coupe.objects.filter(vehicle=listing.vehicle).delete()
    veh_models.SUV.objects.filter(vehicle=listing.vehicle).delete()