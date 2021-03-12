from django.test import TestCase
from agents.models import Agent

class AgentModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Agent.objects.create(
            name="Test_agent",
            photo="photos/2021/03/11/MainPhoto_orig.jpg",
            description="Product test description",
            phone='123456789',
            email='test@text.com',
        )

    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.name, "Test_agent")
        
    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.photo, "photos/2021/03/11/MainPhoto_orig.jpg")
        
    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.description, "Product test description")
        
    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.phone, "123456789")
        
    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.email, "test@text.com")
        
    def test_product_name(self):
        agent = Agent.objects.get(id=1)
        self.assertEqual(agent.is_mvp, False)
        
