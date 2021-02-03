import os
from django.contrib.gis.utils import LayerMapping
from .models import EDOMEX


# Auto-generated `LayerMapping` dictionary for EDOMEX model
edomex_mapping = {
    'cve_ent': 'CVE_ENT',
    'cve_mun': 'CVE_MUN',
    'cvegeo': 'CVEGEO',
    'nomgeo': 'NOMGEO',
    'geom': 'MULTIPOLYGON',
}


mex_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'shp/Edomex.shp'))

def run(verbose = True):
    lm = LayerMapping(EDOMEX, mex_shp, edomex_mapping, transform= False, encoding= 'iso-8859-1')
    lm.save(strict=True, verbose=verbose)