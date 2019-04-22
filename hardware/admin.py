from django.contrib import admin

# Register your models here.
from .models import NISTVendorOption, NISTOperatingSystemOption, NISTHardwareOption, Vendor, Hardware, OperatingSystem
from .forms import HardwareForm, OperatingSystemForm
from applications.models import Application

admin.site.register(NISTVendorOption)
admin.site.register(NISTOperatingSystemOption)
admin.site.register(NISTHardwareOption)
class ApplicationInline(admin.TabularInline):
    model = Application.hardware.through
class VulnerabilityInline(admin.TabularInline):
    model = OperatingSystem.vulnerability.through

class HardwareAdmin(admin.ModelAdmin):
    model = Hardware
    form = HardwareForm
    inlines = [ApplicationInline]
admin.site.register(Hardware, HardwareAdmin)

class OperatingSystemAdmin(admin.ModelAdmin):
    model = OperatingSystem
    form = OperatingSystemForm
    inlines = [VulnerabilityInline]
admin.site.register(OperatingSystem, OperatingSystemAdmin)
