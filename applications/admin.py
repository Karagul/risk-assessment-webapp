from django.contrib import admin

# Register your models here.
from .models import NISTApplicationOption, Application
from .forms import ApplicationForm

admin.site.register(NISTApplicationOption)
class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    form = ApplicationForm
admin.site.register(Application, ApplicationAdmin)