# Urls to manufacturer pages

from django.urls import path

from . import views


app_name = 'manufacturer'
urlpatterns = [
    path('choose-manufacturer/', views.choose_manufacturer, name='choose_manufacturer'),
    path('choose-edit-manufacturer/<int:listing>/', views.choose_edit_manufacturer, name='edit_manufacturer'),
    path('add-manufacturer/', views.add_manufacturer, name='add_manufacturer'),
    path('add-edit-manufacturer/<int:listing>/', views.add_edit_manufacturer, name='add_edit_manufacturer'),
]
