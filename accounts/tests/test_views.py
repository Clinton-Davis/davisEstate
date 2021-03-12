from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestAccountsViews(TestCase):
    
       
    def test_Register_view(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/register.html')
        
    def test_login_view(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/login.html')
        
    def test_dashboard_view(self):
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/dashboard.html')
        
    def test_logout_post(self):
        response = self.client.post(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
        
    
    