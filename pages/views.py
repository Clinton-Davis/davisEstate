from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from agents.models import Agent

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.HTML', context)    

def about(request):
    agent = Agent.objects.order_by('-hire-date')
    mvp_agent = Agent.objects.all().filter(is_mvp=True)
    context = {
        'agents': agent,
        'mvp_agents': mvp_agent
    }
    return render(request, 'pages/about.HTML', context)    
