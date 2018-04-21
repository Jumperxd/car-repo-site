# Logic for user accounts

from django.contrib import messages
from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, redirect, reverse

from . import forms as acc_forms, constants as acc_const, models as acc_models


@transaction.atomic
def create_user(request):
    """This view will contain logic to create a user"""
    formset = formset_factory(acc_forms.ProfilePhoneNumberForm,
                              min_num=acc_const.PHONE_NUMBER_FORMSET_MIN_NUM,
                              validate_min=True,
                              extra=acc_const.PHONE_NUMBER_FORMSET_EXTRA)
    if request.method == 'POST':
        user_form = acc_forms.UserForm(request.POST)
        profile_form = acc_forms.ProfileForm(request.POST)
        phone_number_formset = formset(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and phone_number_formset.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            user.refresh_from_db()
            profile_form = acc_forms.ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            profile = user.profile.__dict__; del profile['_state']
            profile = acc_models.Profile.objects.get(**profile)
            for form in phone_number_formset:
                phone_number = form.save(commit=False)
                phone_number.profile = profile
                phone_number.save()
            return redirect(reverse('index'))
        else:
            messages.error(request, acc_const.SIGNUP_ERROR_MESSAGE)
    else:
        user_form = acc_forms.UserForm()
        profile_form = acc_forms.ProfileForm()
        phone_number_formset = formset()
    context = {
        'title': acc_const.USER_CREATION_TITLE,
        'user_form': user_form,
        'profile_form': profile_form,
        'phone_number_formset': phone_number_formset,
    }
    return render(request, 'account/signup.html', context)
