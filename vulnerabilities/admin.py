from django.contrib import admin

from .models import NISTCVE, VulnerableCPE, Vulnerability

admin.site.register(NISTCVE)
admin.site.register(VulnerableCPE)
admin.site.register(Vulnerability)

