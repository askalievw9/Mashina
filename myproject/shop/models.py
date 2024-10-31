from django.db import models


class Marka(models.Model):
  marka_name = models.CharField(max_length=16, unique=True)

  def __str__(self):
    return self.marka_name


class Model(models.Model):
  model_name = models.CharField(max_length=32)
  marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

  def __str__(self):
    return self.model_name


class Car(models.Model,):
  title = models.CharField(max_length=100)
  description = models.TextField()
  marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  color = models.CharField(max_length=20)
  volume = models.DecimalField(max_digits=2, decimal_places=1)
  year = models.PositiveIntegerField()
  type_change = models.BooleanField()
  image = models.ImageField(upload_to='img/', null=True, blank=True)
  video = models.FileField(upload_to='vid/', null=True, blank=True)

  def __str__(self):
    return self.title
