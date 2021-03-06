from django.db import models
from datetime import datetime



class Contact (models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    agent_name = models.CharField(max_length=200)
    agent_email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Valuation(models.Model):
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    request_date = models.DateTimeField(default=datetime.now, blank=True)
    valuation_completed = models.BooleanField(default=False)
   
    
    def __str__(self):
        return self.name