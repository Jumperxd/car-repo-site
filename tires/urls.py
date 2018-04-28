# URL patterns for tires

from django.urls import path

from . import views


app_name = 'tires'
urlpatterns = [
    path('choose-tires/<int:vehicle>/', views.choose_tires, name='choose_tires'),
    path('choose-edit-tires/<int:listing>/', views.choose_edit_tires, name='choose_edit_tires'),
    path('add-tires/<int:vehicle>/', views.add_tires, name='add_tires'),
    path('add-edit-tires/<int:listing>/', views.add_edit_tires, name='add_edit_tires'),
]
