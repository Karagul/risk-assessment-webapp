from django.contrib import admin

from .models import BusinessRole, SystemRole
from activities.models import SystemActivity
class SystemActivityInline(admin.TabularInline):
    model = SystemActivity
class SystemRoleAdmin(admin.ModelAdmin):
    model = SystemRole
    inlines = [SystemActivityInline]
admin.site.register(SystemRole, SystemRoleAdmin)

admin.site.register(BusinessRole)
