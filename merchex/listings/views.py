
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste des annonces</h1>')

def contact_us(request):
    return HttpResponse('<h1></h1><p>Contactez-nous à l\'adresse suivante : <a href="mailto:amirworms@gmail.com">Mail de contact</a><p>')