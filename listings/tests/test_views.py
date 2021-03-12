from django.test import TestCase, Client
from django.shortcuts import reverse
from listings.models import Listing
from agents.models import Agent

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.agent = Agent.objects.create(
            pk=1,
            name='Deven Kou',
            photo='photos/2021/03/11/MainPhoto_orig.jpg',
            description='Peter Kui is a distinguished',
            phone= '086 678876',
            email= 'deven@davisestates.com',
            is_mvp=False,
            hire_date= '2012-03-11T13:47:43Z',
        )
        self.listing1 = Listing.objects.create(
            pk=1,
            agent=self.agent,
            land_type='House',
            address='Greenvale',
            city='Skerries',
            county='Co. Dublin',
            postcode='K34 WD36',
            price=930000,
            bedrooms=5,
            bathrooms=5,
            parking=True,
            sqm=262,
            ber='D2',
            photo_main='photos/2021/03/11/main1.webp',
            list_date='2021-03-11T15:07:40Z'
        )
        self.listing_url = reverse('listings:listings')
        self.search_url = reverse('listings:search')
        self.listing_detail_url = reverse('listings:list_details', args=[1])
       
    def test_listings_view_GET(self):
        response = self.client.get(self.listing_url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('listings' in response.context)
        self.assertTemplateUsed(response,'listings/listings.html')
        
    def test_listings_details_view_GET(self):
        response = self.client.get(self.listing_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'listings/list_detail.html')
        
        
    def test_search_view_GET(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('listings' in response.context)
        self.assertTrue('bedroom_choices' in response.context)
        self.assertTrue('price_choices' in response.context)
        self.assertTemplateUsed(response,'listings/search.html')
        
    
        