from django.shortcuts import render
from listings.models import Listing
from agents.models import Agent
from listings.selectChoices import bedroom_choices, price_choices, county_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    agent = Agent.objects.order_by('-hire_date')
    mvp_agent = Agent.objects.all().filter(is_mvp=True)
    context = {
        'agents': agent,
        'mvp_agent': mvp_agent
    }
    return render(request, 'pages/about.html', context)
