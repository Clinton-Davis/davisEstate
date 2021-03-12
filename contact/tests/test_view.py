from django.test import TestCase, Client
from django.shortcuts import reverse


class TestContactViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.sell_url = reverse('contacts:sell')
    
    def test_contacts_sell_page_GET(self):
        response = self.client.get(self.sell_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'contacts/sell.html')
        
        