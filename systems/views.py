from django.views import generic
from django.shortcuts import render

from .models import System
class IndexView(generic.ListView):
    template_name = 'systems/index.html'
    context_object_name = 'systems'

    def get_queryset(self):
        """Return the last five published questions."""
        return System.objects.all()


class DetailView(generic.DetailView):
    model = System
    template_name = 'systems/detail.html'


class ResultsView(generic.DetailView):
    model = System
    template_name = 'polls/results.html'