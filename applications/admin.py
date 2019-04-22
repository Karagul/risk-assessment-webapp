from django.contrib import admin

# Register your models here.
from .models import NISTApplicationOption, Application
from vulnerabilities.models import Vulnerability
from .forms import ApplicationForm

admin.site.register(NISTApplicationOption)
class VulnerabilityInline(admin.TabularInline):
    model = Application.vulnerability.through
class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    form = ApplicationForm
    inlines = [VulnerabilityInline]
admin.site.register(Application, ApplicationAdmin)