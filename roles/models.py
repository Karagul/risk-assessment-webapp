from django.db import models

from systems.models import System
class SystemRole(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    # Foreign keys
    system = models.ForeignKey(System, on_delete=models.CASCADE)


    class Meta:
        db_table = 'system_role'

    def __str__(self):
        return self.name

class BusinessRole(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    # Foreign keys
    system_role = models.ManyToManyField(SystemRole, blank=True, null=True)
    # business_activity = models.ManyToManyField(BusinessActivity, blank=True, null=True)


    class Meta:
        db_table = 'business_role'

    def __str__(self):
        return self.name
        
