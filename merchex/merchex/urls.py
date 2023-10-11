"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views as listings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', listings_views.band_list, name="band-list"),
    path('bands/<int:band_id>/', listings_views.band_detail, name="band-detail"),
    path('bands/<int:band_id>/listings', listings_views.band_listings, name="band-listings"),
    path('listings/', listings_views.listing_list, name="listings-list"),
    path('listings/<int:listing_id>/', listings_views.listing_detail, name="listings-detail"),
    path('contact_us/', listings_views.contact_us, name='contact'),
    path('success_email/', listings_views.email_sent, name='email-sent'),
    path('about_us', listings_views.about, name="about"),
  ]
