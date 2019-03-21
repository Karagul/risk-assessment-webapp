from django.contrib import admin

# Register your models here.
from .models import NISTVendorOption, NISTOperatingSystemOption, NISTHardwareOption, Vendor, Hardware, OperatingSystem
from .forms import HardwareForm, OperatingSystemForm

admin.site.register(NISTVendorOption)
admin.site.register(NISTOperatingSystemOption)
admin.site.register(NISTHardwareOption)

class HardwareAdmin(admin.ModelAdmin):
    model = Hardware
    form = HardwareForm
admin.site.register(Hardware, HardwareAdmin)

class OperatingSystemAdmin(admin.ModelAdmin):
    model = OperatingSystem
    form = OperatingSystemForm
admin.site.register(OperatingSystem, OperatingSystemAdmin)
