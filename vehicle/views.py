# Vehicle app logic

from account import models as acc_models

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, reverse
from django.views import View

from carRepo import constants as main_const

from . import forms as veh_forms, constants as veh_const, models as veh_models, utils as veh_utils


@login_required
@transaction.atomic
def add_vehicle(request, **kwargs):
    """Adds a vehicle to the database"""
    if request.method == 'POST':
        vehicle_form = veh_forms.VehicleForm(request.POST)
        vehicle_type_form = veh_forms.VehicleTypeForm(request.POST)
        if vehicle_form.is_valid() and vehicle_type_form.is_valid():
            vehicle = vehicle_form.save()
            veh_models.VehicleManufacturer.objects.create(manufacturer_id=kwargs['manufacturer'], vehicle=vehicle)
            vehicle_type = vehicle_type_form.cleaned_data['vehicle_type']
            if vehicle_type == veh_const.SEDAN:
                return redirect(reverse('vehicle:add_sedan', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.TRUCK:
                return redirect(reverse('vehicle:add_truck', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.COUPE:
                return redirect(reverse('vehicle:add_coupe', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.SUV:
                return redirect(reverse('vehicle:add_suv', kwargs={'vehicle': vehicle.id}))
            return redirect(reverse('powertrain:choose_powertrain', kwargs={'vehicle': vehicle.id}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        vehicle_form = veh_forms.VehicleForm()
        vehicle_type_form = veh_forms.VehicleTypeForm()
    context = {
        'title': veh_const.ADD_VEHICLE_TITLE,
        'vehicle_form': vehicle_form,
        'vehicle_type_form': vehicle_type_form,
    }
    return render(request, 'vehicle/add_vehicle.html', context)


@login_required
@transaction.atomic
def edit_vehicle(request, **kwargs):
    """Edit Listed Vehicle"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        vehicle_form = veh_forms.VehicleForm(request.POST, instance=listing.vehicle)
        vehicle_type_form = veh_forms.VehicleTypeForm(request.POST)
        if vehicle_form.is_valid() and vehicle_type_form.is_valid():
            vehicle_form.save()
            vehicle_type = vehicle_type_form.cleaned_data['vehicle_type']
            if vehicle_type:
                veh_utils.delete_associated_subclass(listing, vehicle_type)
            if vehicle_type == veh_const.SEDAN:
                return redirect(reverse('vehicle:edit_sedan', kwargs={'listing': kwargs['listing'],
                                                                      'vehicle_type': veh_const.SEDAN,
                                                                      'new': 1}))
            elif vehicle_type == veh_const.TRUCK:
                return redirect(reverse('vehicle:edit_truck', kwargs={'listing': kwargs['listing'],
                                                                      'vehicle_type': veh_const.TRUCK,
                                                                      'new': 1}))
            elif vehicle_type == veh_const.COUPE:
                return redirect(reverse('vehicle:edit_coupe', kwargs={'listing': kwargs['listing'],
                                                                      'vehicle_type': veh_const.COUPE,
                                                                      'new': 1}))
            elif vehicle_type == veh_const.SUV:
                return redirect(reverse('vehicle:edit_suv', kwargs={'listing': kwargs['listing'],
                                                                    'vehicle_type': veh_const.SUV,
                                                                    'new': 1}))
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        vehicle_form = veh_forms.VehicleForm(instance=listing.vehicle)
        vehicle_type_form = veh_forms.VehicleTypeForm()
    context = {
        'title': veh_const.EDIT_VEHICLE_TITLE,
        'vehicle_form': vehicle_form,
        'vehicle_type_form': vehicle_type_form,
        'listing': kwargs['listing'],
    }
    return render(request, 'vehicle/edit_vehicle.html', context)


class AddVehicleSubclass(View, LoginRequiredMixin):
    """This class based view will handle any vehicle subclasses with adding"""
    template = 'main/generic_form.html'
    context = {}
    form_class = None

    def get(self, request, **kwargs):
        """Code that will be executed from a get request"""
        form = self.form_class()
        self.context['form'] = form
        return render(request, self.template, self.context)

    @transaction.atomic
    def post(self, request, **kwargs):
        """Code that will be executed from a post request"""
        form = self.form_class(request.POST)
        self.context['form'] = form
        if form.is_valid():
            sub_vehicle = form.save(commit=False)
            sub_vehicle.vehicle_id = kwargs['vehicle']
            sub_vehicle.save()
            return redirect(reverse('powertrain:choose_powertrain', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
        return render(request, self.template, self.context)


class EditVehicleSubclass(View, LoginRequiredMixin):
    """This class based view will handle updating vehicle subclasses"""
    template = 'vehicle/edit_vehicle_subclass.html'
    context = {}
    form_class = None

    @staticmethod
    def determine_subclass(listing, vehicle_type, new):
        """Helper function to get correct instance from database"""
        if new:
            return None
        if vehicle_type == veh_const.SEDAN:
            return listing.vehicle.sedan
        elif vehicle_type == veh_const.TRUCK:
            return listing.vehicle.truck
        elif vehicle_type == veh_const.COUPE:
            return listing.vehicle.coupe
        return listing.vehicle.suv

    @transaction.atomic
    def get(self, request, **kwargs):
        """Code that will be executed from a get request"""
        listing = acc_models.List.objects.get(pk=kwargs['listing'])
        subclass = self.determine_subclass(listing, kwargs['vehicle_type'], kwargs['new'])
        form = self.form_class(instance=subclass)
        self.context['listing'] = kwargs['listing']
        self.context['form'] = form
        return render(request, self.template, self.context)

    @transaction.atomic
    def post(self, request, **kwargs):
        """Code that will be executed from a post request"""
        listing = acc_models.List.objects.get(pk=kwargs['listing'])
        subclass = self.determine_subclass(listing, kwargs['vehicle_type'], kwargs['new'])
        form = self.form_class(request.POST, instance=subclass)
        self.context['listing'] = kwargs['listing']
        self.context['form'] = form
        if form.is_valid():
            sub_vehicle = form.save(commit=False)
            sub_vehicle.vehicle = listing.vehicle
            sub_vehicle.save()
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
        return render(request, self.template, self.context)


def vehicle_details(request, **kwargs):
    """Display Details of a Vehicle"""
    account = User.objects.get(pk=kwargs['account'])
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    context = {
        'title': veh_const.VEHICLE_DETAILS_TITLE,
        'account': account,
        'listing': listing,
    }
    return render(request, 'vehicle/vehicle_details.html', context)
