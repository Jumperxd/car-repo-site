# Logic for powertrain functions

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, reverse

from carRepo import constants as main_const

from . import forms as pow_forms, constants as pow_const


@login_required
def choose_powertrain(request, **kwargs):
    """This view contains logic for choosing a powertrain already in database"""
    if request.method == 'POST':
        form = pow_forms.ChoosePowerTrainForm(request.POST)
        if form.is_valid():
            return redirect(reverse())
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
def add_powertrain(request, **kwargs):
    """This view contains logic for adding a new powertrain to the database"""
    if request.method == 'POST':
        form = pow_forms.PowerTrainForm(request.POST)
        if form.is_valid():
            powertrain = form.save(commit=False)
            powertrain.vehicle = kwargs['vehicle']
            powertrain.save()
            return redirect(reverse())
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = pow_forms.PowerTrainForm()
    context = {
        'title': pow_const.ADD_POWERTRAIN_TITLE,
        'form': form
    }
    return render(request, 'main/generic_form.html', context)
