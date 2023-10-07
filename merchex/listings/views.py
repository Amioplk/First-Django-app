
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def contact_us(request):
    return render(request, 'listings/contact.html')