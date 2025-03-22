import os
from typing import Optional

project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))

import geopandas as gpd
from .downloads_geral import _prepare_cache

def download_malha_geosampa(name_feature, cache_path:str, paginate:bool=False, sort_by:Optional[str]=None):

    if paginate and not sort_by:
        print('Cuidado que talvez voce precise definir uma coluna de indice. A API retorna um documento com um erro e não dá status code correto!')
    
    url = ("http://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs?version=1.0.0"
            "&request=GetFeature&outputFormat=SHAPE-ZIP"
           f"&typeName=geoportal:{name_feature}")
    
    gdf= _prepare_cache(url, name_feature, cache_path, paginate, sort_by=sort_by)
    return gdf