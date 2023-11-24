from django.db import models
from django.conf import settings

class Recommend(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    deposit = models.IntegerField()
    saving = models.IntegerField()
  
