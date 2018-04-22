# Urls related to vehicles

from django.urls import path

from . import views


app_name = 'vehicle'
urlpatterns = [
    path('choose_vehicle/', views.choose_vehicle, name='choose_vehicle'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
]
