from django.db import models

# Create your models here.
from edc_model.models import BaseUuidModel, HistoricalRecords

from .visit import Visit

class CrfModel(BaseUuidModel):

    visit = models.OneToOneField(Visit)

    # objects = CrfModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.visit.natural_key(), )
    natural_key.dependencies = ['app1.visit']