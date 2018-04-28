# Logic for user accounts

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, reverse

from carRepo import constants as main_const

from . import forms as acc_forms, constants as acc_const, models as acc_models


@transaction.atomic
def create_user(request):
    """This view will contain logic to create a user"""
    if request.method == 'POST':
        user_form = acc_forms.UserForm(request.POST)
        profile_form = acc_forms.ProfileForm(request.POST)
        phone_number_formset = acc_forms.PhoneNumberFormset(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and phone_number_formset.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            user.refresh_from_db()
            profile_form = acc_forms.ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_obj = profile_form.save()
            for form in phone_number_formset:
                phone_number = form.save(commit=False)
                phone_number.profile = profile_obj
                phone_number.save()
            return redirect(reverse('index'))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        user_form = acc_forms.UserForm()
        profile_form = acc_forms.ProfileForm()
        phone_number_formset = acc_forms.PhoneNumberFormset()
    context = {
        'title': acc_const.USER_CREATION_TITLE,
        'user_form': user_form,
        'profile_form': profile_form,
        'phone_number_formset': phone_number_formset,
    }
    return render(request, 'account/signup.html', context)


@login_required
@transaction.atomic
def edit_profile(request):
    """Logic to update a user account"""
    if request.method == 'POST':
        user_form = acc_forms.EditUserForm(request.POST, instance=request.user)
        profile_form = acc_forms.ProfileForm(request.POST, instance=request.user.profile)
        phone_number_formset = acc_forms.PhoneNumberFormset(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and phone_number_formset.is_valid():
            acc_models.ProfilePhoneNumbers.objects.filter(profile=request.user.profile).delete()
            user_form.save()
            profile_obj = profile_form.save()
            for form in phone_number_formset:
                phone_number = form.save(commit=False)
                phone_number.profile = profile_obj
                phone_number.save()
            return redirect(reverse('account:profile'))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        phone_numbers = list(acc_models.ProfilePhoneNumbers.objects.filter(
            profile=request.user.profile).values('number_type', 'phone_number'))
        user_form = acc_forms.EditUserForm(instance=request.user)
        profile_form = acc_forms.ProfileForm(instance=request.user.profile)
        phone_number_formset = acc_forms.PhoneNumberFormset(initial=phone_numbers)
    context = {
        'title': acc_const.EDIT_ACCOUNT_TITLE,
        'user_form': user_form,
        'profile_form': profile_form,
        'phone_number_formset': phone_number_formset,
    }
    return render(request, 'account/signup.html', context)


@login_required
@transaction.atomic
def delete_account(request):
    """Logic to delete a users account"""
    user = User.objects.get(pk=request.user.id)
    logout(request)
    user.delete()
    return redirect(reverse('index'))


@login_required
def profile(request):
    """Display a user profile."""
    phone_numbers = acc_models.ProfilePhoneNumbers.objects.filter(profile=request.user.profile)
    listings = acc_models.List.objects.filter(profile=request.user.profile)
    context = {
        'title': acc_const.USER_PROFILE_TITLE,
        'delete_account_message': acc_const.ACCOUNT_DELETION_MESSAGE,
        'delete_all_listings_message': acc_const.ALL_LIST_DELETE_MESSAGE,
        'delete_listing_message': acc_const.LIST_DELETE_MESSAGE,
        'phone_numbers': phone_numbers,
        'listings': listings,
    }
    return render(request, 'account/profile.html', context)


@login_required
@transaction.atomic
def list_vehicle(request, **kwargs):
    """This view contains logic used to list a vehicle"""
    if request.method == 'POST':
        form = acc_forms.ListVehicleForm(request.POST)
        if form.is_valid():
            list_data = form.save(commit=False)
            list_data.profile = request.user.profile
            list_data.vehicle_id = kwargs['vehicle']
            list_data.save()
            messages.success(request, acc_const.LIST_SUCCESS_MESSAGE)
            return redirect(reverse('account:profile'))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = acc_forms.ListVehicleForm()
    context = {
        'title': acc_const.LIST_VEHICLE_TITLE,
        'form': form,
    }
    return render(request, 'main/generic_form.html', context)


@login_required
@transaction.atomic
def delete_all_listings(request):
    """Logic to delete all listings a user has"""
    acc_models.List.objects.filter(profile=request.user.profile).delete()
    return redirect(reverse('account:profile'))


@login_required
@transaction.atomic
def delete_listing(request, **kwargs):
    """Logic to delete a specific listing"""
    acc_models.List.objects.filter(pk=kwargs['listing']).delete()
    return redirect(reverse('account:profile'))
