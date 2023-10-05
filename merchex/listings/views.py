
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <p>Mes annonces :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
    """)

def contact_us(request):
    return HttpResponse('<h1></h1><p>Contactez-nous à l\'adresse suivante : <a href="mailto:amirworms@gmail.com">Mail de contact</a><p>')