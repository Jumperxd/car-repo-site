# Urls related to vehicles

from django.urls import path

from . import views, forms, constants as veh_const


app_name = 'vehicle'
urlpatterns = [
    path('add-vehicle/<int:manufacturer>/', views.add_vehicle, name='add_vehicle'),
    path('edit-vehicle/<int:listing>/', views.edit_vehicle, name='edit_vehicle'),
    path('add-sedan/<int:vehicle>/',
         views.AddVehicleSubclass.as_view(
             form_class=forms.SedanForm,
             context={
                 'title': veh_const.ADD_SEDAN_TITLE,
             }
         ),
         name='add_sedan'),
    path('add-truck/<int:vehicle>/',
         views.AddVehicleSubclass.as_view(
             form_class=forms.TruckForm,
             context={
                 'title': veh_const.ADD_TRUCK_TITLE,
             }
         ),
         name='add_truck'),
    path('add-coupe/<int:vehicle>/',
         views.AddVehicleSubclass.as_view(
             form_class=forms.CoupeForm,
             context={
                 'title': veh_const.ADD_COUPE_TITLE,
             }
         ),
         name='add_coupe'),
    path('add-suv/<int:vehicle>/',
         views.AddVehicleSubclass.as_view(
             form_class=forms.SUVForm,
             context={
                 'title': veh_const.ADD_SUV_TITLE,
             }
         ),
         name='add_suv'),
    path('edit-sedan/<int:listing>/<str:vehicle_type>/<int:new>/',
         views.EditVehicleSubclass.as_view(
             form_class=forms.SedanForm,
             context={
                 'title': veh_const.EDIT_SEDAN_TITLE,
             }
         ),
         name='edit_sedan'),
    path('edit-truck/<int:listing>/<str:vehicle_type>/<int:new>/',
         views.EditVehicleSubclass.as_view(
             form_class=forms.TruckForm,
             context={
                 'title': veh_const.EDIT_TRUCK_TITLE,
             }
         ),
         name='edit_truck'),
    path('edit-coupe/<int:listing>/<str:vehicle_type>/<int:new>/',
         views.EditVehicleSubclass.as_view(
             form_class=forms.CoupeForm,
             context={
                 'title': veh_const.EDIT_COUPE_TITLE,
             }
         ),
         name='edit_coupe'),
    path('edit-suv/<int:listing>/<str:vehicle_type>/<int:new>/',
         views.EditVehicleSubclass.as_view(
             form_class=forms.SUVForm,
             context={
                 'title': veh_const.EDIT_SUV_TITLE,
             }
         ),
         name='edit_suv'),
    path('vehicle-details/<int:account>/<int:listing>/', views.vehicle_details, name='vehicle_details'),
]
