from django import forms
from apps.vehiculos.models import Vehiculo

class vehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo

        fields = [
            'modelo',
            'color',
            'placa',
            'motor',
            'marca',
            'tipovehiculo',
        ]

        labels = {
            'modelo': 'Ingrese el Modelo',
            'color': 'Ingrese el Color',
            'placa': 'Ingrese el Placa',
            'motor': 'Ingrese el Motor',
            'marca': 'Ingrese el Marca',
            'tipovehiculo': 'Ingrese el Tipo vehiculo',
        }

        Widget = {
            'modelo': forms.TextInput(attrs={'class': 'forms-control'}),
            'color': forms.TextInput(attrs={'class': 'forms-control'}),
            'placa': forms.TextInput(attrs={'class': 'forms-control'}),
            'motor': forms.TextInput(attrs={'class': 'forms-control'}),
            'marca': forms.Select(attrs={'class': 'forms-control'}),
            'tipovehiculo': forms.Select(attrs={'class': 'forms-control'}),
        }