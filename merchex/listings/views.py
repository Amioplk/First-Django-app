
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
          'listings/band_detail.html',
          {'band': band})

def band_listings(request, id):
    band = Band.objects.get(id=id)
    return render(request,
          'listings/band_listings.html',
          {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings_list.html', {'listings': listings})

def listings_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request,
                  'listings/listings_detail.html',
                  {'listing': listing})

def contact_us(request):
    return render(request, 'listings/contact.html')