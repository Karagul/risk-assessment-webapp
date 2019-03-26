from django.contrib import admin

from .models import BusinessRole, SystemRole

admin.site.register(BusinessRole)
admin.site.register(SystemRole)
