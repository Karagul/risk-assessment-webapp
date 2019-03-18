from django.contrib import admin

# Register your models here.
from .models import NISTVendorOption, NISTOperatingSystemOption, NISTHardwareOption, Vendor, Hardware, OperatingSystem

admin.site.register(NISTVendorOption)
admin.site.register(NISTOperatingSystemOption)
admin.site.register(NISTHardwareOption)


admin.site.register(Vendor)
admin.site.register(OperatingSystem)
admin.site.register(Hardware)
