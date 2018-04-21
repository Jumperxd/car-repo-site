# Register models to admin site.

from django.contrib import admin

from . import models


admin.site.register(models.Tires)
