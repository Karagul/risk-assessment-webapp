from dal import autocomplete, forward

from django import forms
from hardware.models import NISTVendorOption
from .models import Application, NISTApplicationOption

class ApplicationForm(forms.ModelForm):
    vendor = forms.ModelChoiceField(
        queryset=NISTVendorOption.objects.all(),
        widget=autocomplete.ModelSelect2(url='hardware:vendor-autocomplete')
    )
    application = forms.ModelChoiceField(
        queryset=NISTApplicationOption.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='applications:application-autocomplete',
            forward=(
                'vendor',
            )
        )
    )
    # version = forms.ModelChoiceField(
        # queryset=NISTApplicationOption.objects.all(),
        # widget=autocomplete.ModelSelect2(
            # url='applications:application-autocomplete',
            # forward=(
                # 'vendor',
            # )
        # )
    # )
    class Meta:
        model = Application
        fields = ('label', 'description', 'note', 'vendor', 'hardware',)