from django.shortcuts import render

# Create your views here.
from dal import autocomplete

from django.views import generic
from .models import Hardware, OperatingSystem
from .models import NISTVendorOption, NISTHardwareOption, NISTOperatingSystemOption


class IndexView(generic.ListView):
    template_name = 'hardware/index.html'
    context_object_name = 'hardware'

    def get_queryset(self):
        """Return the last five published questions."""
        return Hardware.objects.all()

class DetailView(generic.DetailView):
    model = Hardware
    template_name = 'hardware/detail.html'

class OSDetailView(generic.DetailView):
    model = OperatingSystem
    template_name = 'hardware/detail.html'

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
            return qs

        return qs

class OperatingSystemAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return NISTOperatingSystemOption.objects.none()

        qs = NISTOperatingSystemOption.objects.all().order_by('product')

        vendor = self.forwarded.get('vendor', None)

        if vendor:
            qs = qs.filter(vendor=vendor)

        if self.q:
            qs = qs.filter(product__istartswith=self.q)
            return qs

        return qs