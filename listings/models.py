from django.db import models
from datetime import datetime
from agents.models import Agent
from ckeditor.fields import RichTextField


class Listing(models.Model):
    LAND_TYPE_CHOICES = (
        ('House', 'House'),
        ('Apartment' , 'Apartment'),
        ('Duplex', 'Duplex')
    )
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    land_type = models.CharField(max_length=20, choices=LAND_TYPE_CHOICES)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.BooleanField(default=False)
    sqm = models.IntegerField()
    ber = models.CharField(max_length=2, default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    sale_agreed = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.address
