import os
project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))

import geopandas as gpd
from logging import (
    Logger,
    getLogger,
)

from .downloads_geral import (
    _prepare_cache,
    set_cache_path
)

def download_malha_geosampa(name_feature, cache_path:str, paginate:bool=False):
    cache_path = set_cache_path(data_path)
    url = f"""http://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=geoportal:{name_feature}"""
    gdf= _prepare_cache(url, name_feature, cache_path, paginate)
    return gdf

 

def paginated_download(name_feature, data_path, logger:Logger=getLogger()):
    cache_path = set_cache_path(data_path)
    cache_full_path = os.path.join(
        cache_path,
        f'{name_feature}_concat.parquet'
    )

    if os.path.exists(
        cache_full_path
    ):
        logger.info("Carregando arquivo em cache")
        gdf = gpd.read_parquet(cache_full_path)
    else:
        gdf = download_malha_geosampa(
            name_feature,
            cache_path,
            True
        )

    return gdf
