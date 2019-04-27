from django.db import models

from roles.models import BusinessRole, SystemRole
from infoassets.models import InfoAssetGroup
from applications.models import Application
from hardware.models import OperatingSystem

class BusinessActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    # Foreign keys
    business_role = models.ManyToManyField(BusinessRole, blank=True)


    class Meta:
        db_table = 'business_activity'

    def __str__(self):
        return self.name

class SystemActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    monthly_value = models.DecimalField(max_digits=12, decimal_places=2)
    # Foreign keys
    business_activity = models.ForeignKey(BusinessActivity, on_delete=models.CASCADE, blank=True, null=True)
    system_role = models.ManyToManyField(SystemRole)
    info_asset_group = models.ManyToManyField(InfoAssetGroup)
    application = models.ManyToManyField(Application)
    operating_system = models.ManyToManyField(OperatingSystem)


    class Meta:
        db_table = 'system_activity'

    def __str__(self):
        return self.name
