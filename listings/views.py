from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

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
     return render(request, 'listings/list_detail.html', {})
    
def search(request):
     return render(request, 'listings/search.html', {})
