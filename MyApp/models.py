from django.db import models

# Create your models here.

class Asset(models.Model):
    name = models.CharField(max_length=50) # type: ignore
    description = models.TextField()
    Value = models.IntegerField()
    image = models.ImageField(upload_to="pics")
    available = models.BooleanField()
