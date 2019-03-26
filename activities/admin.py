from django.contrib import admin

from .models import BusinessActivity, SystemActivity

admin.site.register(BusinessActivity)
admin.site.register(SystemActivity)
