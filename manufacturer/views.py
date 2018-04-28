# Logic used with manufacturers

from account import models as acc_models

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, reverse, redirect

from carRepo import constants as main_const

from vehicle import models as veh_models

from . import forms as man_forms, constants as man_const, models as man_models


@login_required
def choose_manufacturer(request):
    """This view contains logic in choosing a pre-existing manufacturer"""
    if request.method == 'POST':
        form = man_forms.ChooseManufacturerForm(request.POST)
        if form.is_valid():
            return redirect(reverse('vehicle:add_vehicle',
                                    kwargs={'manufacturer': form.cleaned_data['manufacturer'].id}))
        else:
            messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = man_forms.ChooseManufacturerForm()
    context = {
        'title': man_const.CHOOSE_MANUFACTURER_TITLE,
        'form': form,
    }
    return render(request, 'manufacturer/choose_manufacturer.html', context)


@login_required
@transaction.atomic
def add_manufacturer(request):
    """Add a new manufacturer to database"""
    if request.method == 'POST':
        manufacturer_form = man_forms.ManufacturerForm(request.POST)
        phone_number_formset = man_forms.PhoneNumberFormset(request.POST)
        if manufacturer_form.is_valid() and phone_number_formset.is_valid():
            manufacturer = manufacturer_form.save(commit=False).__dict__
            del manufacturer['_state']
            manufacturer, created = man_models.Manufacturer.objects.get_or_create(**manufacturer)
            for phone_number_form in phone_number_formset:
                phone_number = phone_number_form.save(commit=False)
                phone_number.manufacturer = manufacturer
                phone_number.save()
            return redirect(reverse('vehicle:add_vehicle', kwargs={'manufacturer': manufacturer.id}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        manufacturer_form = man_forms.ManufacturerForm()
        phone_number_formset = man_forms.PhoneNumberFormset()
    context = {
        'title': man_const.ADD_MANUFACTURER_TITLE,
        'manufacturer_form': manufacturer_form,
        'phone_number_formset': phone_number_formset,
    }
    return render(request, 'manufacturer/add_manufacturer.html', context)


@login_required
@transaction.atomic
def choose_edit_manufacturer(request, **kwargs):
    """Logic to choose a new manufacturer on listing"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        form = man_forms.ChooseManufacturerForm(request.POST)
        if form.is_valid():
            veh_models.VehicleManufacturer.objects.filter(
                vehicle=listing.vehicle).update(manufacturer_id=form.cleaned_data['manufacturer'])
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = man_forms.ChooseManufacturerForm()
    context = {
        'title': man_const.CHOOSE_MANUFACTURER_TITLE,
        'form': form,
        'listing': kwargs['listing'],
    }
    return render(request, 'manufacturer/choose_edit_manufacturer.html', context)


@login_required
@transaction.atomic
def add_edit_manufacturer(request, **kwargs):
    """Logic to add a new manufacturer in updating a listing"""
    listing = acc_models.List.objects.get(pk=kwargs['listing'])
    if request.method == 'POST':
        manufacturer_form = man_forms.ManufacturerForm(request.POST)
        phone_number_formset = man_forms.PhoneNumberFormset(request.POST)
        if manufacturer_form.is_valid() and phone_number_formset.is_valid():
            manufacturer = manufacturer_form.save(commit=False).__dict__
            del manufacturer['_state']
            manufacturer, created = man_models.Manufacturer.objects.get_or_create(**manufacturer)
            for phone_number_form in phone_number_formset:
                phone_number = phone_number_form.save(commit=False)
                phone_number.manufacturer = manufacturer
                phone_number.save()
            veh_models.VehicleManufacturer.objects.filter(vehicle=listing.vehicle).update(manufacturer=manufacturer)
            return redirect(reverse('account:edit_listing', kwargs={'listing': kwargs['listing']}))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        manufacturer_form = man_forms.ManufacturerForm()
        phone_number_formset = man_forms.PhoneNumberFormset()
    context = {
        'title': man_const.ADD_MANUFACTURER_TITLE,
        'manufacturer_form': manufacturer_form,
        'phone_number_formset': phone_number_formset,
        'listing': kwargs['listing']
    }
    return render(request, 'manufacturer/add_edit_manufacturer.html', context)
