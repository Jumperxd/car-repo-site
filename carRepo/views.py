# This file contains the logic the home page will follow upon loading

from django.shortcuts import render

from . import constants as main_const


def index(request):
    """This view will pass basic information for the home page"""
    context = {
        'title': main_const.INDEX_TITLE,
    }
    return render(request, 'main/index.html', context)
