from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, redirect

from . import forms as acc_forms, constants as acc_const

# Create your views here.


@transaction.atomic
def create_user(request):
    """This view will contain logic to create a user"""
    if request.method == 'POST':
        user_form = acc_forms.UserForm(request.POST)
        profile_form = acc_forms.ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form = acc_forms.ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
    else:
        user_form = acc_forms.UserForm()
        profile_form = acc_forms.ProfileForm()
    context = {
        'title': acc_const.USER_CREATION_TITLE,
        'user_form': user_form,
        'profile_form': profile_form,
    }
