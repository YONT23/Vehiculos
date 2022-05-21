from django import forms
from apps.ventas.models import Venta, vehiculoventa

class ventaForm(forms.ModelForm):
    class Meta:
        model = Venta

        fields = [
            'fecha',
            'valorTotal',
            'tipoPago',
            'user',
            #'vehiculo',
            #'venta',
            #'cantidad',
            #'precio',
#
        ]

        labels = {
            'fecha': 'Ingrese la Fecha',
            'valorTotal': 'Ingrese el Valor total',
            'tipoPago': 'Ingrese el Tipo de pago',
            'user': 'Ingrese el Usuario',
            #'vehiculo': 'Select el vehiculo',
            #'venta': 'Ingrese la venta',
            #'cantidad': 'Ingrese la cantidad',
            #'precio': 'Ingrese el precio',
        }#

        Widget = {
            'fecha': forms.DateInput(),
            'valorTotal': forms.NumberInput(attrs={'class': 'forms-control'}),
            'tipoPago':forms.TextInput(attrs={'class': 'forms-control'}),
            'tipoPago':forms.Select(attrs={'class': 'forms-control'}),
            #'vehiculo':forms.Select(attrs={'class': 'forms-control'}),
            #'cantidad':forms.TextInput(attrs={'class': 'forms-control'}),
        }