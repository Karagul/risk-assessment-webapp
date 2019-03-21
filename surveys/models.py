from django.db import models
from django.contrib.auth import get_user_model

from systems.models import System

class Survey(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    # Foreign keys
    system = models.ManyToManyField(System)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    class Meta:
        db_table = 'survey'

    def __str__(self):
        return self.name
