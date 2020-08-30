#models

# basic_api/models.py
from django.db import models

#Plist
class Plist(models.Model):
    number = models.BigIntegerField()
    isPrime = models.BooleanFields()
    lastUpdate = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name