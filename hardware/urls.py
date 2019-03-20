from django.urls import path

from .views import VendorAutocomplete, HardwareAutocomplete


app_name = 'hardware'
urlpatterns = [
    path('vendor-autocomplete/', VendorAutocomplete.as_view(), name='vendor-autocomplete'),
    path('hardware-autocomplete/', HardwareAutocomplete.as_view(), name='hardware-autocomplete'),
]