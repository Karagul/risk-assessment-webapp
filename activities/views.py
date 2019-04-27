from django.shortcuts import render
from django.views import generic

from .models import SystemActivity
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'activities/index.html'
    context_object_name = 'activities'

    def get_queryset(self):
        """Return the last five published questions."""
        return SystemActivity.objects.all()

class DetailView(generic.DetailView):
    model = SystemActivity
    template_name = 'activities/detail.html'
