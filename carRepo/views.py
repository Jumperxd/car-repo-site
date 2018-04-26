# This file contains the logic the home page will follow upon loading

from account import models as acc_models

from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import render, redirect, reverse

from . import constants as main_const, forms as main_forms, utils as main_utils


def index(request):
    """This view will pass basic information for the home page"""
    average_price = acc_models.List.objects.all().aggregate(Avg('car_value'))
    context = {
        'title': main_const.INDEX_TITLE,
        'average_price': average_price['car_value__avg'],
    }
    return render(request, 'main/index.html', context)


def find_all_listings(request):
    """The logic to find all listings in database"""
    listings = acc_models.List.objects.all()
    context = {
        'title': main_const.FIND_ALL_LISTINGS_TITLE,
        'listings': listings,
    }
    return render(request, 'main/display_listings.html', context)


def advanced_search(request):
    """The logic in filtering listings based on certain parameters"""
    if request.method == 'POST':
        form = main_forms.AdvancedSearchForm(request.POST)
        if form.is_valid():
            listings = main_utils.determine_listings(form)
            if listings:
                context = {
                    'title': main_const.ADVANCED_SEARCH_RESULTS_TITLE,
                    'listings': listings,
                }
                return render(request, 'main/display_listings.html', context)
            return redirect(reverse('find_all_listings'))
        messages.error(request, main_const.ERROR_MESSAGE)
    else:
        form = main_forms.AdvancedSearchForm()
    context = {
        'title': main_const.ADVANCED_SEARCH_TITLE,
        'form': form,
    }
    return render(request, 'main/generic_form.html', context)
