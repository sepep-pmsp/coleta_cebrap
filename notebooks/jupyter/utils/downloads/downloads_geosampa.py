import os
project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
print(project_path)


import geopandas as gpd
from .downloads_geral import _prepare_cache

def download_malha_geosampa(name_feature, paginate:bool=False):
    url = f"""http://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=geoportal:{name_feature}"""
    gdf= _prepare_cache(url, name_feature, paginate)
    return gdf