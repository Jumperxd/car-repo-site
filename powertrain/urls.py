# URL patterns for the powertrain app

from django.urls import path

from . import views


app_name = 'powertrain'
urlpatterns = [
    path('choose-powertrain/<int:vehicle>/', views.choose_powertrain, name='choose_powertrain'),
    path('add-powertrain/<int:vehicle>/', views.add_powertrain, name='add_powertrain'),
]
