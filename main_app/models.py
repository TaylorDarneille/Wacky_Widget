from django.db import models

# Create your models here.
class Item(models.Model):
  description = models.CharField(max_length=100)

class Quantity(models.Model):
  quantity = models.IntegerField(max_length=100)