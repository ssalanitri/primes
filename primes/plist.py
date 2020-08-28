from django.db import models

# Create your models here.
class Plist(models.Model):
    id = models.IntegerField()
    number = models.BigIntegerField()
    isPrime = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created']