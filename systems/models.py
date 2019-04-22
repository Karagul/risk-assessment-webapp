from django.db import models

from hardware.models import Hardware

# Create your models here.
class System(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    is_third_party = models.BooleanField(default=False)

    # Foreign keys
    hardware = models.ManyToManyField(Hardware)
    #add system role


    class Meta:
        db_table = 'system'

    def __str__(self):
        return self.name
