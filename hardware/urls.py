from django.urls import path

from . import views

app_name = 'hardware'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('os/<int:pk>/', views.OSDetailView.as_view(), name='os_detail'),
    path('vendor-autocomplete/', views.VendorAutocomplete.as_view(), name='vendor-autocomplete'),
    path('hardware-autocomplete/', views.HardwareAutocomplete.as_view(), name='hardware-autocomplete'),
    path('operating-system-autocomplete/', views.OperatingSystemAutocomplete.as_view(), name='operating-system-autocomplete'),
]