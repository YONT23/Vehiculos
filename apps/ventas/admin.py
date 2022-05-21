from django.contrib import admin
from apps.ventas.models import Venta, vehiculoventa


# Register your models here.

class MenbershipInline(admin.TabularInline):
    model = vehiculoventa
    extra = 1
    
class VentaAdmin(admin.ModelAdmin):
    inlines = (MenbershipInline,)
    list_display = ('fecha', 'valorTotal', 'tipoPago','user')
    ordering = ('fecha', 'valorTotal', 'tipoPago','user')
    search_fields = ('fecha','valorTotal','tipoPago','user')
    list_filter = ('fecha','valorTotal','tipoPago','user')

admin.site.register(Venta, VentaAdmin)
#admin.site.register(vehiculoventa)