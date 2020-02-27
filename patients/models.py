from django.db import models
import random

class Patient(models.Model):

  # Fields
  #
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

  # calculate for raw data
  def save(self, *args, **kwargs):
    # here to do calculation for raw data (produce random for simple case)
    self.sbp = random.randint(100,130)
    self.dbp = random.randint(70,90)
    self.hr = random.randint(60,90)
    super().save(*args, **kwargs) # real save method (must add!!)
    