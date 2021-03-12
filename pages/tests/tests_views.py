from django.test import TestCase, Client
from django.shortcuts import reverse
from listings.models import Listing
from agents.models import Agent


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('pages:index')
        self.about_url = reverse('pages:about')
    
    def test_home_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('listings' in response.context)
        self.assertTrue('bedroom_choices' in response.context)
        self.assertTrue('price_choices' in response.context)
        self.assertTemplateUsed(response,'pages/index.html')
        
    def test_about_page_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('agents' in response.context)
        self.assertTrue('mvp_agent' in response.context)
        self.assertTemplateUsed(response,'pages/about.html')
        

        

        

