from django.test import TestCase, Client
from django.shortcuts import reverse
from listings.models import Listing
from agents.models import Agent

class TestViews(TestCase):
   
       
    def test_listings_page_GET(self):
        response = self.client.get(reverse('listings:listings'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('listings' in response.context)
        self.assertTemplateUsed(response,'listings/listings.html')
        
        
        