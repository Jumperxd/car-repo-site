# Register models to django admin site.

from django.contrib import admin

from . import models


admin.site.register(models.Manufacturer)
admin.site.register(models.ManufacturerPhoneNumbers)
