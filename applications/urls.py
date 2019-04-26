from django.urls import path


from . import views

app_name = 'applications'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('application-autocomplete/', views.ApplicationAutocomplete.as_view(), name='application-autocomplete'),
]
