from django.test import TestCase
from contact.models import Contact, Valuation

class ContactModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(
            listing='testListing',
            listing_id='1',
            name='tester',
            email='tester@texter.com',
            phone='123456789',
            message='Testing the message',
            user_id='1',
            agent_name='testeragent',
            agent_email='agent@mail.com',
        )

    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.listing, "testListing")
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.listing_id, "1")
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.name, "tester")
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.email, "tester@texter.com")
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.phone, "123456789")
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.message, 'Testing the message')
    def test_product_name(self):
        
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.user_id, '1')
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.agent_name, 'testeragent')
        
    def test_product_name(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.agent_email, 'agent@mail.com')
        
