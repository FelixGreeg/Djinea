from django.conf.urls import url,include
from .views import casa, edomex_datasets,ineageojson,webmapi,estadis,rutasmap


urlpatterns = [
    url(r'^$',casa.as_view(template_name='inicio.html'),name='home'),
    #url(r'^$',HomePageView.as_view(template_name='index.html'),name='home'),
    url(r'Mapaweb',webmapi.as_view(template_name='webmap.html'),name='home'),
    url(r'Rutas',rutasmap.as_view(template_name='rutas.html'),name='home'),
    url(r'Estadistica',estadis,name='home'),
    url(r'edomex',edomex_datasets,name='edomex'),
    url(r'unidades',ineageojson,name='unidades')
]