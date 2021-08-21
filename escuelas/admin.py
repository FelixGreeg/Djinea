from django.contrib.gis import admin

# Register your models here.
from escuelas.models import Unidad_Operativa,Coordinaciones,Municipios,Localidades,EDOMEX
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin



admin.site.site_title = 'SIGINEA'
admin.site.site_header = ' Instituto Nacional para la Educación de los Adultos'
admin.site.index_title = "Bienvenidos al portal de administración"


class mapAdmin(LeafletGeoAdmin):#proyección esférica de Mercator 
   # inlines=[coorInline,munInline,locInline]
    list_display=('Clave_Unidad_Operativa','Nombre_Unidad_Operativa','Tipo_Unidad_Operativa',"Municipio")
    search_fields=('Clave_Unidad_Operativa','Nombre_Unidad_Operativa')
    ordering=('Clave_Unidad_Operativa','Nombre_Unidad_Operativa','Tipo_Unidad_Operativa',"Municipio")
    list_filter=['Coordinación']
    filter_horizontal=()
    fieldsets=()
    #pass
    # Configuración para OSMGeoAdmin #
    #default_zoom=8
    #default_lon= -11095966.37748
    #default_lat= 2188721.75418
    #map_width= 1000
    #map_height= 500

class EdomexAdmin(LeafletGeoAdmin):
    list_display=('cvegeo','nomgeo')
    search_fields=[('nomgeo')]

admin.site.register(Unidad_Operativa,mapAdmin)
admin.site.register(EDOMEX,EdomexAdmin)


#admin.site.register(Municipios)
#admin.site.register(Localidades)
#admin.site.register(Coordinaciones)
