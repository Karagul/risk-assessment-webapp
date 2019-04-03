from django.contrib import admin

from .models import System
from roles.models import SystemRole

# Register your models here.
class SystemRoleInline(admin.TabularInline):
    model = SystemRole
class SystemAdmin(admin.ModelAdmin):
    model = System
    inlines = [SystemRoleInline]
admin.site.register(System, SystemAdmin)