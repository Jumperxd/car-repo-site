# Urls related to vehicles

from django.urls import path

from . import views, forms, constants as veh_const


app_name = 'vehicle'
urlpatterns = [
    path('choose-vehicle/', views.choose_vehicle, name='choose_vehicle'),
    path('add-vehicle/<int:manufacturer>/', views.add_vehicle, name='add_vehicle'),
    path('choose-sedan/<int:vehicle>/',
         views.ChooseVehicleSubClass.as_view(
             form_class=forms.ChooseSedanForm,
             context = {
                 'title': veh_const.CHOOSE_SEDAN_TITLE,
                 'vehicle_subclass': 'Sedan',
                 'subclass_url': 'vehicle:add-sedan',
             },
        ),
        name='choose-sedan'),
    path('choose-truck/<int:vehicle>/',
         views.ChooseVehicleSubClass.as_view(
             form_class=forms.ChooseTruckForm,
             context = {
                 'title': veh_const.CHOOSE_TRUCK_TITLE,
                 'vehicle_subclass': 'Truck',
                 'subclass_url': 'vehicle:add-truck',
             },
        ),
        name='choose-truck'),
    path('choose-coupe/<int:vehicle>/',
         views.ChooseVehicleSubClass.as_view(
             form_class=forms.ChooseCoupeForm,
             context = {
                 'title': veh_const.CHOOSE_COUPE_TITLE,
                 'vehicle_subclass': 'Coupe',
                 'subclass_url': 'vehicle:add-coupe',
             },
        ),
        name='choose-coupe'),
    path('choose-suv/<int:vehicle>/',
         views.ChooseVehicleSubClass.as_view(
             form_class=forms.ChooseSUVForm,
             context = {
                 'title': veh_const.CHOOSE_SUV_TITLE,
                 'vehicle_subclass': 'SUV',
                 'subclass_url': 'vehicle:add-suv',
             },
        ),
        name='choose-suv'),
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
]
