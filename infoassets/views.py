from django.shortcuts import render
from django.views import generic

from .models import InfoAssetGroup

class IndexView(generic.ListView):
    template_name = 'infoassets/index.html'
    context_object_name = 'infoassets'

    def get_queryset(self):
        """Return the last five published questions."""
        return InfoAssetGroup.objects.all()

class DetailView(generic.DetailView):
    model = InfoAssetGroup
    template_name = 'infoassets/detail.html'