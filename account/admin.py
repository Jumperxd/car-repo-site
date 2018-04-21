# Register Models to Django admin site.

from django.contrib import admin

from . import models


admin.site.register(models.Profile)
admin.site.register(models.ProfilePhoneNumbers)
admin.site.register(models.List)
