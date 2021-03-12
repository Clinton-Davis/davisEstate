from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from listings.selectChoices import bedroom_choices, price_choices


def listings(request):
     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
     paginator = Paginator(listings, 6)
     page = request.GET.get('page')
     page_listings = paginator.get_page(page)
     context = {
          'listings' : page_listings,
     }
     return render(request, 'listings/listings.html', context)
    
def list_details(request, listing_id):
     listing = get_object_or_404(Listing, pk=listing_id)
     context = {
          'listing': listing,
     }
     return render(request, 'listings/list_detail.html', context)
    
def search(request):
     queryset_list = Listing.objects.order_by('-list_date')
     #Keywords
     if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
           queryset_list = queryset_list.filter(description__icontains=keywords)
     #City
     if 'city' in request.GET:
        city = request.GET['city']
        if city:
           queryset_list = queryset_list.filter(city__iexact=city)
     #County
     if 'county' in request.GET:
        county = request.GET['county']
        if county:
           queryset_list = queryset_list.filter(county__iexact=county)
     #Bedrooms
     if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
           queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
     #Price
     if 'price' in request.GET:
        price = request.GET['price']
        if price:
           queryset_list = queryset_list.filter(price__lte=price)
     context = {
     'bedroom_choices': bedroom_choices,
     'price_choices': price_choices,
     'listings': queryset_list,
     'values': request.GET,
     }
     return render(request, 'listings/search.html', context)
