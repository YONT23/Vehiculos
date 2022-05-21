from django.shortcuts import render, redirect
from apps.vehiculos.form import vehiculoForm
from apps.vehiculos.models import Vehiculo

# Create your views here.

def listVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-id')
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculos/listVehiculos.html',context)

def home(request):
    return render(request, 'base/base.html')

def vehiculosCreate(request):
    if request.method == 'POST':
        form = vehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listvehiculos')
    else:
        form = vehiculoForm()
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculosUpdate(request, id_vehiculo):
    mant = Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'GET':
        form = vehiculoForm(instance=mant)
    else:
        form = vehiculoForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listvehiculos')
    
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculosDelete(request, id_vehiculo):
    mant = Vehiculo.objects.get(pk=id_vehiculo)
    if request.method == 'POST':
       mant.delete()
       return redirect('vehiculos:listvehiculos')
    return render(request, 'vehiculos/vehiculosDelete.html', {'vehiculo': mant})