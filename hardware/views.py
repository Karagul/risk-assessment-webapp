from django.shortcuts import render

# Create your views here.
from dal import autocomplete

from .models import NISTVendorOption, NISTHardwareOption


class VendorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return NISTVendorOption.objects.none()

        qs = NISTVendorOption.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
class HardwareAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return NISTHardwareOption.objects.none()

        qs = NISTHardwareOption.objects.all().order_by('product')

        vendor = self.forwarded.get('vendor', None)

        if vendor:
            qs = qs.filter(vendor=vendor)

        if self.q:
            qs = qs.filter(product__istartswith=self.q)
            print(qs.query)
            return qs

        return qs