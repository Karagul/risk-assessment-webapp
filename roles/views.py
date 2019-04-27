from django.shortcuts import render
from django.views import generic

from .models import SystemRole

class IndexView(generic.ListView):
    template_name = 'roles/index.html'
    context_object_name = 'roles'

    def get_queryset(self):
        """Return the last five published questions."""
        return SystemRole.objects.all()

class DetailView(generic.DetailView):
    model = SystemRole
    template_name = 'roles/detail.html'
