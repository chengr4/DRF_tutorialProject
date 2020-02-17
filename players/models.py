from django.db import models

class Paradigm(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Player(models.Model):
  name = models.CharField(max_length=50)
  country = models.CharField(max_length=50, default='country/region')
  paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Programmer(models.Model):
  name = models.CharField(max_length=50)
  players = models.ManyToManyField(Player)

  def __str__(self):
    return self.name

  
