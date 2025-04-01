import os
from typing import Optional

project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))

import geopandas as gpd
from .downloads_geral import _prepare_cache


def paginated_load_cache(
    cache_path:str, 
    name_feature:str,
    url:str,
    paginate:bool,
    sort_by:Optional[str]=None
):
    
    cache_full_path = os.path.join(
        cache_path,
        f'{name_feature}_concat.parquet'
    )

    if paginate and os.path.exists(cache_full_path):
        print('Carregando arquivo em cache')
        gdf = gpd.read_parquet(cache_full_path)
    else:
        gdf= _prepare_cache(url, name_feature, cache_path, paginate, sort_by=sort_by)
    
    return gdf


def download_malha_geosampa(
    name_feature, 
    data_path:str, 
    paginate:bool=False, 
    sort_by:Optional[str]=None):

    cache_path = os.path.join(
        data_path,
        'cache'
    )

    if paginate and not sort_by:
        print('Cuidado que talvez voce precise definir uma coluna de indice. A API retorna um documento com um erro e não dá status code correto!')
    
    url = ("http://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs?version=1.0.0"
            "&request=GetFeature&outputFormat=SHAPE-ZIP"
           f"&typeName=geoportal:{name_feature}")
    
    gdf=paginated_load_cache(cache_path, name_feature, url, paginate, sort_by=sort_by)

    return gdf