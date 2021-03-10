from django.test import TestCase

class TestViews(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='pages/index.html')
        

        

        

