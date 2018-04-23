# URL patterns for tires

from django.urls import path

from . import views


app_name = 'tires'
urlpatterns = [
    path('choose-tires/<int:vehicle>/', views.choose_tires, name='choose_tires'),
    path('add-tires/<int:vehicle>/', views.add_tires, name='add_tires'),
]
