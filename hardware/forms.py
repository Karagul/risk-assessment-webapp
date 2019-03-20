from dal import autocomplete, forward

from django import forms
from .models import NISTVendorOption, Hardware, NISTHardwareOption


class HardwareForm(forms.ModelForm):
    vendor = forms.ModelChoiceField(
        queryset=NISTVendorOption.objects.all(),
        widget=autocomplete.ModelSelect2(url='hardware:vendor-autocomplete')
    )
    hardware = forms.ModelChoiceField(
        queryset=NISTHardwareOption.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='hardware:hardware-autocomplete',
            forward=(
                'vendor',
            )
        )
    )

    class Meta:
        model = Hardware
        fields = ('label', 'description', 'note', 'vendor',)
        