from django.urls import path
from apps.ventas.views import listventas, ventasCreate, ventasUpdate, ventasDelete

app_name= 'ventas'
urlpatterns = [
    path('', listventas, name= 'listventas'),
    path('nuevo2/', ventasCreate, name= 'ventasCreate'),
    path('actualizar/<int:id_Venta>/', ventasUpdate, name= 'ventasUpdate'),
    path('eliminar/<int:id_Venta>/', ventasDelete, name= 'ventasDelete'),
]