# Vehicle app logic

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, redirect, reverse
from django.views import View

from carRepo import constants as main_const

from . import forms as veh_forms, constants as veh_const


@login_required
def choose_vehicle(request):
    """Choose a vehicle currently in database"""
    if request.method == 'POST':
        form = veh_forms.ChooseVehicleForm(request.POST)
        if form.is_valid():
            return redirect(reverse('account:list_vehicle',
                                    kwargs={'vehicle': form.cleaned_data['vehicle'].id}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = veh_forms.ChooseVehicleForm()
    context = {
        'title': veh_const.CHOOSE_VEHICLE_TITLE,
        'form': form,
    }
    return render(request, 'vehicle/choose_vehicle.html', context)


@login_required
@transaction.atomic
def add_vehicle(request, **kwargs):
    """Adds a vehicle to the database"""
    if request.method == 'POST':
        vehicle_form = veh_forms.VehicleForm(request.POST)
        vehicle_type_form = veh_forms.VehicleTypeForm(request.POST)
        if vehicle_form.is_valid() and vehicle_type_form.is_valid():
            vehicle = vehicle_form.save(commit=False)
            vehicle.manufacturer = kwargs['manufacturer']
            vehicle = vehicle.save()
            vehicle_type = vehicle_type_form.cleaned_data['vehicle_type']
            if vehicle_type == veh_const.SEDAN:
                return redirect(reverse('vehicle:choose-sedan', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.TRUCK:
                return redirect(reverse('vehicle:choose-truck', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.COUPE:
                return redirect(reverse('vehicle:choose-coupe', kwargs={'vehicle': vehicle.id}))
            elif vehicle_type == veh_const.SUV:
                return redirect(reverse('vehicle:choose-suv', kwargs={'vehicle': vehicle.id}))
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


class ChooseVehicleSubClass(View, LoginRequiredMixin):
    """This class based view will handle any vehicle subclasses with choosing"""
    template = 'vehicle/choose_vehicle_subclass.html'
    context = {}
    form_class = None

    def get(self, request, **kwargs):
        """Code that will be executed with a get request"""
        form = self.form_class()
        self.context['form'] = form
        self.context['vehicle'] = kwargs['vehicle']
        return render(request, self.template, self.context)

    def post(self, request, **kwargs):
        """Code that will be executed with a post request"""
        form = self.form_class(request.POST)
        self.context['form'] = form
        if form.is_valid():
            return redirect(reverse('powertrain:choose_powertrain', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
        return render(request, self.template, self.context)


class AddVehicleSubclass(View, LoginRequiredMixin):
    """This class based view will handle any vehicle subclasses with adding"""
    template = 'main/generic_form.html'
    context = {}
    form_class = None

    def get(self, request):
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
            sub_vehicle.vehicle = kwargs['vehicle']
            sub_vehicle.save()
            return redirect(reverse('powertrain:choose_powertrain', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
        return render(request, self.template, self.context)
