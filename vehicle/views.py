# Vehicle app logic

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, reverse

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
        else:
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
        form = veh_forms.VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.manufacturer = kwargs['manufacturer']
            vehicle.save()
            return redirect(reverse())
        else:
            messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = veh_forms.VehicleForm()
    context = {
        'title': veh_const.ADD_VEHICLE_TITLE,
        'form': form,
    }
    return render(request, 'main/generic_form.html', context)
