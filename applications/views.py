from django.shortcuts import render
from dal import autocomplete

from .models import NISTApplicationOption
# Create your views here.

class ApplicationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return NISTApplicationOption.objects.none()

        qs = NISTApplicationOption.objects.all().order_by('product')

        vendor = self.forwarded.get('vendor', None)

        if vendor:
            qs = qs.filter(vendor=vendor)

        if self.q:
            qs = qs.filter(product__istartswith=self.q)
            return qs

        return qs