from django.shortcuts import render

def listings(request):
     return render(request, 'listings/listings.html', {})
    
def listdetails(request):
     return render(request, 'listings/list_details.html', {})
    
def search(request):
     return render(request, 'listings/search.html', {})
