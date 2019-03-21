from django.urls import path

from .views import ApplicationAutocomplete

app_name = 'applications'
urlpatterns = [
    path('application-autocomplete/', ApplicationAutocomplete.as_view(), name='application-autocomplete'),
]
