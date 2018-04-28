# Logic for powertrain functions

from account import models as acc_models

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, reverse

from carRepo import constants as main_const

from . import forms as pow_forms, constants as pow_const, models as pow_models


@login_required
@transaction.atomic
def choose_powertrain(request, **kwargs):
    """This view contains logic for choosing a powertrain already in database"""
    if request.method == 'POST':
        form = pow_forms.ChoosePowerTrainForm(request.POST)
        if form.is_valid():
            pow_models.VehiclePowerTrain.objects.create(vehicle_id=kwargs['vehicle'],
                                                        powertrain=form.cleaned_data['powertrain'])
            return redirect(reverse('tires:choose_tires', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = pow_forms.ChoosePowerTrainForm()
    context = {
        'title': pow_const.CHOOSE_POWERTRAIN_TITLE,
        'form': form,
        'vehicle': kwargs['vehicle']
    }
    return render(request, 'powertrain/choose_powertrain.html', context)


@login_required
@transaction.atomic
def choose_edit_powertrain(request, **kwargs):
    """Logic to choose a new powertrain to put on a listed vehicle"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        form = pow_forms.ChoosePowerTrainForm(request.POST)
        if form.is_valid():
            pow_models.VehiclePowerTrain.objects.filter(
                vehicle=listing.vehicle).update(powertrain_id=form.cleaned_data['powertrain'])
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = pow_forms.ChoosePowerTrainForm()
    context = {
        'title': pow_const.CHOOSE_POWERTRAIN_TITLE,
        'form': form,
        'listing': kwargs['listing'],
    }
    return render(request, 'powertrain/choose_edit_powertrain.html', context)


@login_required
@transaction.atomic
def add_powertrain(request, **kwargs):
    """This view contains logic for adding a new powertrain to the database"""
    if request.method == 'POST':
        form = pow_forms.PowerTrainForm(request.POST)
        if form.is_valid():
            powertrain = form.save(commit=False)
            del powertrain['_state']
            powertrain, created = pow_models.PowerTrain.objects.get_or_create(**powertrain)
            pow_models.VehiclePowerTrain.objects.create(vehicle_id=kwargs['vehicle'], powertrain=powertrain)
            return redirect(reverse('tires:choose_tires', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = pow_forms.PowerTrainForm()
    context = {
        'title': pow_const.ADD_POWERTRAIN_TITLE,
        'form': form
    }
    return render(request, 'main/generic_form.html', context)


@login_required
@transaction.atomic
def add_edit_powertrain(request, **kwargs):
    """Logic to add a new powertrain in updating a listing"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        form = pow_forms.PowerTrainForm(request.POST)
        if form.is_valid():
            powertrain = form.save(commit=False)
            del powertrain['_state']
            powertrain, created = pow_models.PowerTrain.objects.get_or_create(**powertrain)
            pow_models.VehiclePowerTrain.objects.filter(vehicle=listing.vehicle).update(powertrain=powertrain)
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = pow_forms.PowerTrainForm()
    context = {
        'title': pow_const.ADD_POWERTRAIN_TITLE,
        'form': form,
        'listing': kwargs['listing'],
    }
    return render(request, 'powertrain/add_edit_powertrain.html', context)
