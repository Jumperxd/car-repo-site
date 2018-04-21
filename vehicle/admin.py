# Register models to admin site.

from django.contrib import admin

from . import models


admin.site.register(models.Vehicle)
admin.site.register(models.Coupe)
admin.site.register(models.Sedan)
admin.site.register(models.Truck)
admin.site.register(models.SUV)
