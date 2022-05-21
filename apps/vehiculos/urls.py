from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculosCreate, vehiculosUpdate, vehiculosDelete 

app_name= 'vehiculos'
urlpatterns = [
    path('', listVehiculos, name= 'listvehiculos'),
    path('nuevo/', vehiculosCreate, name= 'vehiculosCreate'),
    path('actualizar/<int:id_vehiculo>/', vehiculosUpdate, name= 'vehiculosUpdate'),
    path('eliminar/<int:id_vehiculo>/', vehiculosDelete, name= 'vehiculosDelete'),
]