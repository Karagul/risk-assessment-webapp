from django.db import models

from roles.models import BusinessRole, SystemRole
from infoassets.models import InfoAssetGroup

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
    # Foreign keys
    business_activity = models.ForeignKey(BusinessActivity, on_delete=models.CASCADE, blank=True, null=True)
    system_role = models.ForeignKey(SystemRole, on_delete=models.CASCADE, blank=True, null=True)
    info_asset_group = models.ManyToManyField(InfoAssetGroup)


    class Meta:
        db_table = 'system_activity'

    def __str__(self):
        return self.name
