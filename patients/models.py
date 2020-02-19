from django.db import models

class Patient(models.Model):

  # Fields
  name = models.CharField(max_length=10)
  sbp_raw = models.IntegerField(default=0)
  dbp_raw = models.IntegerField(default=0)
  hr_raw = models.IntegerField(default=0)
  sbp = models.IntegerField(default=0)
  dbp = models.IntegerField(default=0)
  hr = models.IntegerField(default=0)

  # Methods
  def __str__(self):
    return self.name
