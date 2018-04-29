# Logic for tires functions

from account import models as acc_models

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, reverse

from carRepo import constants as main_const

from . import forms as tire_forms, constants as tire_const, models as tire_models


@login_required
@transaction.atomic
def choose_tires(request, **kwargs):
    """A view that will handle the logic of choosing pre-existing tires"""
    if request.method == 'POST':
        form = tire_forms.ChooseTiresForm(request.POST)
        if form.is_valid():
            tire_models.VehicleTires.objects.create(vehicle_id=kwargs['vehicle'], tires=form.cleaned_data['tires'])
            return redirect(reverse('account:list_vehicle', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = tire_forms.ChooseTiresForm()
    context = {
        'title': tire_const.CHOOSE_TIRES_TITLE,
        'form': form,
        'vehicle': kwargs['vehicle'],
    }
    return render(request, 'tires/choose_tires.html', context)


@login_required
@transaction.atomic
def choose_edit_tires(request, **kwargs):
    """A view that will handle the logic of choosing pre-existing tires"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        form = tire_forms.ChooseTiresForm(request.POST)
        if form.is_valid():
            tire_models.VehicleTires.objects.filter(
                vehicle=listing.vehicle).update(tires_id=form.cleaned_data['tires'])
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = tire_forms.ChooseTiresForm()
    context = {
        'title': tire_const.CHOOSE_TIRES_TITLE,
        'form': form,
        'listing': kwargs['listing'],
    }
    return render(request, 'tires/choose_edit_tires.html', context)


@login_required
@transaction.atomic
def add_tires(request, **kwargs):
    """A view that will handle the logic of adding a new tires object to the database"""
    if request.method == 'POST':
        form = tire_forms.TiresForm(request.POST)
        if form.is_valid():
            tires = form.save(commit=False).__dict__
            del tires['_state']
            tires, created = tire_models.Tires.objects.get_or_create(**tires)
            tire_models.VehicleTires.objects.create(vehicle_id=kwargs['vehicle'], tires=tires)
            return redirect(reverse('account:list_vehicle', kwargs={'vehicle': kwargs['vehicle']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = tire_forms.TiresForm()
    context = {
        'title': tire_const.ADD_TIRES_TITLE,
        'form': form,
    }
    return render(request, 'main/generic_form.html', context)


@login_required
@transaction.atomic
def add_edit_tires(request, **kwargs):
    """Logic to add new tires when editing a listing"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        form = tire_forms.TiresForm(request.POST)
        if form.is_valid():
            tires = form.save(commit=False).__dict__
            del tires['_state']
            tires, created = tire_models.Tires.objects.get_or_create(**tires)
            tire_models.VehicleTires.objects.filter(vehicle=listing.vehicle).update(tires=tires)
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = tire_forms.TiresForm()
    context = {
        'title': tire_const.ADD_TIRES_TITLE,
        'form': form,
        'listing': listing,
    }
    return render(request, 'tires/add_edit_tires.html', context)
