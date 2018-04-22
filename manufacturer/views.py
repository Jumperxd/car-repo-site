# Logic used with manufacturers

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, reverse, redirect

from carRepo import constants as main_const

from . import forms as man_forms, constants as man_const


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
    return render(request, 'manufacturer/choosemanufacturer.html', context)


@login_required
@transaction.atomic
def add_manufacturer(request):
    """Add a new manufacturer to database"""
    formset = formset_factory(man_forms.ManufacturerPhoneNumberForm,
                              min_num=man_const.PHONE_NUMBER_MIN_NUM,
                              extra=man_const.PHONE_NUMBER_EXTRA,
                              validate_min=True)
    if request.method == 'POST':
        manufacturer_form = man_forms.ManufacturerForm(request.POST)
        phone_number_formset = formset(request.POST)
        if manufacturer_form.is_valid() and phone_number_formset.is_valid():
            manufacturer = manufacturer_form.save()
            for phone_number_form in phone_number_formset:
                phone_number = phone_number_form.save(commit=False)
                phone_number.manufacturer = manufacturer
                phone_number.save()
            return redirect(reverse('vehicle:add_vehicle', kwargs={'manufacturer': manufacturer.id}))
        else:
            messages.error(request, main_const.ERROR_MESSAGE)
    else:
        manufacturer_form = man_forms.ManufacturerForm()
        phone_number_formset = formset()
    context = {
        'title': man_const.ADD_MANUFACTURER_TITLE,
        'manufacturer_form': manufacturer_form,
        'phone_number_formset': phone_number_formset,
    }
    return render(request, 'manufacturer/addmanufacturer.html', context)
